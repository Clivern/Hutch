# Copyright 2022 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import time

from django_rq import job

from app.cloud import Digitalocean
from app.shortcuts import Logger
from app.service.ansible import Ansible
from app.helpers.configs import get_config
from app.repository import HostRepository
from app.repository import TaskRepository


@job
def deploy_server_on_digitalocean(task_id):
    """
    Deploy Nginx Server on Digitalocean
    """
    start_time = time.time()

    do_status = get_config("digitalocean_status")
    do_token = get_config("digitalocean_api_token")

    logger = Logger().get_logger(__name__)

    runner = Ansible()
    do_client = Digitalocean(do_token)
    host_repository = HostRepository()
    task_repository = TaskRepository()

    logger.info("Run task with id {} in background".format(task_id))

    task = task_repository.get_one_by_id(task_id)

    if not task:
        logger.warning("task with id {} not found".format(task_id))
        return None

    # Get defaults from the server repository
    defaults = {
        "host_id": "",
        "ssh_private_key": "",
        "host_address": "",
        "host_port": 22,
        "host_ssh_key_username": "root",
        "roles": [
            {
                "name": "community/base",
            },
            {
                "name": "community/nginx",
            },
        ],
    }

    defaults.update(json.loads(task.payload))

    host = host_repository.get_one_by_id(defaults["host_id"])

    if not host:
        logger.info(
            "Task has this uuid {} failed since host not found".format(task.uuid)
        )

        duration = (time.time() - start_time) * 1000

        logger.info("Task with uuid {} spent {} millisec".format(task.uuid, duration))

        task_repository.update_one_by_id(
            task.id,
            {
                "result": json.dumps({"errorMessage": "Host not found"}),
                "status": TaskRepository.FAILED,
            },
        )

        return

    defaults["ssh_private_key"] = host.key.private_key
    defaults["host_address"] = host.ipaddress

    output = do_client.get_droplet(host.remote_id)

    if output["status"] == "off":
        do_client.power_on_droplet(output["id"])

    count = 1

    # Wait till server is active
    while output["status"] != "active":
        output = do_client.get_droplet(output["id"])

        count += 1

        if count > 1000:
            logger.info(
                "Task has this uuid {} failed since server is taking too much time to start".format(
                    task.uuid
                )
            )

            duration = (time.time() - start_time) * 1000

            logger.info(
                "Task with uuid {} spent {} millisec".format(task.uuid, duration)
            )

            task_repository.update_one_by_id(
                task.id,
                {
                    "result": json.dumps(
                        {"errorMessage": "Server is taking too much time!"}
                    ),
                    "status": TaskRepository.FAILED,
                },
            )

            return

        time.sleep(10)

    runner.generate(task.uuid, defaults)

    result = runner.run(task.uuid)

    if result:
        logger.info("Task has this uuid {} succeeded".format(task.uuid))
    else:
        logger.info("Task has this uuid {} failed".format(task.uuid))

    duration = (time.time() - start_time) * 1000

    logger.info("Task with uuid {} spent {} millisec".format(task.uuid, duration))

    task_repository.update_one_by_id(
        task.id,
        {
            "result": json.dumps(
                {"successMessage": "Nginx server installed successfully"}
            ),
            "status": TaskRepository.SUCCEEDED if result else TaskRepository.FAILED,
        },
    )
