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
from app.repository import GroupRepository


class HostGroup:
    """HostGroup Class"""

    def __init__(self):
        self.group = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def create(self, data):
        """
        Create a Host Group
        """
        result = self.group.insert_one(data)

        if request:
            self.logger.info(
                "Create a host group with id {} and name {}".format(
                    result.id, result.name
                )
            )

        return result

    def update(self, id, data):
        """
        Update a Host Group By ID
        """
        self.logger.info("Update a host group with id {}".format(id))

        return self.group.update_one_by_id(id, data)

    def delete(self, id):
        """
        Delete a Host Group By ID
        """
        self.logger.info("Delete a host group with id {}".format(id))

        return self.group.delete_one_by_id(id)
