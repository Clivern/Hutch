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

import yaml

from app.shortcuts import Logger
from app.util.file_system import FileSystem


class Plan():
    """Plan Service"""

    def __init__(self):
        self.file_system = FileSystem()
        self.logger = Logger().get_logger(__name__)

    def get_plans(self):
        """
        Returns a list of enabled plans (community and custom ones)

        Returns:
            A list of enabled plans and their requirements
        """
        plans = []

        dirs = self.file_system.list_sub_dirs(self.file_system.app_path(
            "/plan/community"
        ))

        dirs += self.file_system.list_sub_dirs(self.file_system.app_path(
            "/plan/plugin"
        ))

        for d in dirs:
            if not self.file_system.file_exists("{}/info.yml".format(d)):
                continue

            content = self.file_system.read_file("{}/info.yml".format(d))
            data = yaml.safe_load(content)

            if not data['status'] == 'enabled':
                continue

            plans.append(data)

        return plans

    def get_plan_requirements_schema(self, plan):
        """
        Get the plan schema file path

        Args:
            plan: The plan name

        Returns:
            The path to schema file or None
        """
        # Check if it is a community plan
        plan_type = ""
        path1 = self.file_system.app_path("/plan/community/{}".format(plan))
        path2 = self.file_system.app_path("/plan/plugin/{}".format(plan))

        if self.file_system.file_exists("{}/info.yml".format(path1)):
            plan_type = "community"
            content = self.file_system.read_file("{}/info.yml".format(path1))
            data = yaml.safe_load(content)

        elif self.file_system.file_exists("{}/info.yml".format(path2)):
            plan_type = "plugin"
            content = self.file_system.read_file("{}/info.yml".format(path2))
            data = yaml.safe_load(content)

        else:
            raise Exception("Invalid plan {} provided".format(plan))

        # Validate data against requirements
        if data["requirements"]["path"] is None:
            return None

        path = self.file_system.app_path("/plan/{}/{}/{}".format(plan_type, plan, data["requirements"]["path"]))

        if self.file_system.file_exists(path):
            return path

        return None

    def get_plan_requirements_defaults(self, plan):
        """
        Get the plan defaults

        Args:
            plan: The plan name

        Returns:
            The plan defaults or None
        """
        # Check if it is a community plan
        path1 = self.file_system.app_path("/plan/community/{}".format(plan))
        path2 = self.file_system.app_path("/plan/plugin/{}".format(plan))

        if self.file_system.file_exists("{}/info.yml".format(path1)):
            content = self.file_system.read_file("{}/info.yml".format(path1))
            data = yaml.safe_load(content)

        elif self.file_system.file_exists("{}/info.yml".format(path2)):
            content = self.file_system.read_file("{}/info.yml".format(path2))
            data = yaml.safe_load(content)

        else:
            raise Exception("Invalid plan {} provided".format(plan))

        return data["requirements"]["defaults"] if data["requirements"]["defaults"] is None else data["requirements"]["defaults"].strip()
