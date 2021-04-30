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
import ansible_runner

from app.shortcuts import Logger
from app.util.file_system import FileSystem
from django.template.loader import render_to_string


class Ansible():
    """Ansible Service"""

    TEMP_DIR = "tmp"
    CACHE_DIR = "cache"

    def __init__(self):
        """Init Ansible Object"""
        self.logger = Logger().get_logger(__name__)
        self.file_system = FileSystem()

    def generate(self, plan_uuid, configs={}):
        """
        Generate Ansible Plan Files

        Args:
            plan_uuid: the plan uuid
            configs: configs object

        Returns:
            Whether files/dirs got created or not
        """
        self.cleanup(plan_uuid)

        if "host_port" not in configs.keys():
            configs["host_port"] = 22

        if "host_ssh_key_username" not in configs.keys():
            configs["host_ssh_key_username"] = "root"

        if "vars" not in configs.keys():
            configs["vars"] = []

        target_tmp_dir = self.file_system.app_path("/{}/{}/{}".format(self.CACHE_DIR, plan_uuid, self.TEMP_DIR))
        target_hosts_file = self.file_system.app_path("/{}/{}/hosts".format(self.CACHE_DIR, plan_uuid))
        target_playbook_file = self.file_system.app_path("/{}/{}/playbook.yml".format(self.CACHE_DIR, plan_uuid))
        target_private_key_file = self.file_system.app_path("/{}/{}/private_key".format(self.CACHE_DIR, plan_uuid))

        result = self.file_system.create_dirs(target_tmp_dir, 0o775)

        if not result:
            raise Exception("Unable to create a plan {} directories".format(plan_uuid))

        configs["host_ssh_private_key_path"] = target_private_key_file
        configs["plan_uuid"] = plan_uuid

        hosts_file_content = render_to_string("plan/hosts", configs)
        playbook_file_content = render_to_string("plan/playbook", configs)
        private_key_file_content = render_to_string("plan/private_key", configs)

        # Create plan files
        self.file_system.write_file(target_hosts_file, hosts_file_content)
        self.file_system.write_file(target_playbook_file, playbook_file_content)
        self.file_system.write_file(target_private_key_file, private_key_file_content)

        # Change ssh key mode to 600
        self.file_system.change_permission(target_private_key_file, 0o600)

        return True

    def run(self, plan_uuid):
        """
        Run ansible playbook

        Args:
            plan_uuid: The plan uuid

        Returns:
            Whether the run succeeded or not
        """
        data_dir = self.file_system.app_path("/{}/{}/{}".format(self.CACHE_DIR, plan_uuid, self.TEMP_DIR))
        inventory = self.file_system.app_path("/{}/{}/hosts".format(self.CACHE_DIR, plan_uuid))
        playbook = self.file_system.app_path("/{}/{}/playbook.yml".format(self.CACHE_DIR, plan_uuid))

        out = ansible_runner.run(
            private_data_dir=data_dir,
            playbook=playbook,
            inventory=inventory,
            quiet=True
        )

        self.logger.info("Plan with id {} has output: {}".format(plan_uuid, json.dumps(out.stats)))

        if out.status.lower() == "failed":
            self.logger.error("Plan with id {} has failed, output: {}".format(plan_uuid, json.dumps(out.stats)))
            return False

        elif out.status.lower() == "successful":
            return True

        return False

    def cleanup(self, plan_uuid):
        """
        Cleanup plan directory

        Args:
            plan_uuid: The plan uuid
        """
        self.file_system.delete_directory(self.file_system.app_path(
            "/{}/{}".format(self.CACHE_DIR, plan_uuid)
        ))
