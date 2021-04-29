# Copyright 2021 Clivern
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

from app.shortcuts import Logger
from app.repository.task_repository import TaskRepository


@job
def ping(task_id):
    """
    Run Ping Task in Background

    Args:
        task_id: The Async Task ID
    """
    start_time = time.time()
    logger = Logger().get_logger(__name__)

    logger.info("Run task with id {} in background".format(task_id))

    task_repository = TaskRepository()

    task = task_repository.get_one_by_id(task_id)

    if not task:
        logger.info("task with id {} not found".format(task_id))
        return None

    logger.info("Task has this uuid {}".format(task.uuid))
    logger.info("Task with uuid {} succeeded".format(task.uuid))

    duration = (time.time() - start_time) * 1000

    logger.info("Task with uuid {} spent {} millisec".format(task.uuid, duration))

    task_repository.update_one_by_id(task.id, {
        "result": json.dumps({"message": "pong"}),
        "status": TaskRepository.SUCCEEDED
    })
