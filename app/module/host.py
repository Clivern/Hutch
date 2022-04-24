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
from app.repository import HostRepository


class Host:
    """Host Class"""

    def __init__(self):
        self.host = HostRepository()
        self.logger = Logger().get_logger(__name__)

    def get_one_by_id(self, id, user_id):
        """
        Get a Host by ID
        """
        return self.host.get_one_by_id(id, user_id)

    def create(self, data):
        """
        Create a Host
        """
        result = self.host.insert_one(data)

        if result:
            self.logger.info(
                "Create a host with id {} and name {}".format(result.id, result.name)
            )

        return result

    def update(self, id, data):
        """
        Update a Host By ID
        """
        self.logger.info("Update a host with id {}".format(id))

        return self.host.update_one_by_id(id, data)

    def delete_by_id(self, host_id, user_id):
        """
        Delete a Host By ID
        """
        self.logger.info("Delete a host with id {}".format(host_id))

        return self.host.delete_one_by_id(host_id, user_id)

    def get_user_hosts(self, user_id, offset, limit):
        """
        Get User Hosts
        """
        return self.host.get(user_id, offset, limit)

    def count_user_hosts(self, user_id):
        """
        Count User Hosts
        """
        return self.host.count_by_user(user_id)
