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
from app.repository.option_repository import OptionRepository


class Settings:
    """Settings Class"""

    def __init__(self):
        self.logger = Logger().get_logger(__name__)
        self.option_repository = OptionRepository()

    def update_settings(self, settings):
        """
        Update Settings
        """
        for name in settings:
            result = self.option_repository.update_value_by_name(name, settings[name])

            if not result:
                self.option_repository.insert_one(
                    {"name": name, "value": settings[name]}
                )

    def get_settings(self, names):
        """
        Get Many Settings
        """
        options = self.option_repository.get_many_by_names(names)

        result = {}

        for name in names:
            result[name] = ""

        for option in options:
            result[option.name] = option.value

        return result
