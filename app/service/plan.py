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
        pass

    def validate_plan_requirements(self, plan, inputs):
        """
        Validates a plan inputs

        Args:
            plan: The plan name
            inputs: A dict of plan inputs

        Returns:
            Whether they are valid or not
        """
        pass

    def create_plan_payload(self, plan, inputs):
        """
        Creates a plan payload from a valid inputs

        Args:
            plan: The plan name
            inputs: A dict of plan inputs

        Returns:
            A dict of plan payload
        """
        pass
