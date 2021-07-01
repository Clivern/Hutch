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


class Group:
    """Group Class"""

    def __init__(self):
        self.group = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def get_one_by_id(self, id, user_id):
        """
        Get a Group by ID
        """
        return self.group.get_one_by_id(id, user_id)

    def create(self, data):
        """
        Create a Host Group
        """
        result = self.group.insert_one(data)

        if result:
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

    def delete_by_id(self, group_id, user_id):
        """
        Delete a Host Group By ID
        """
        self.logger.info("Delete a host group with id {}".format(group_id))

        return self.group.delete_one_by_id(group_id, user_id)

    def get_user_groups(self, user_id, offset, limit):
        """
        Get User Groups
        """
        return self.group.get(user_id, offset, limit)

    def count_user_groups(self, user_id):
        """
        Get User Groups
        """
        return self.group.count_by_user(user_id)

    def count_hosts_by_group(self, group_id, user_id):
        """
        Count hosts by group id
        """
        return self.group.count_hosts_by_group(group_id, user_id)
