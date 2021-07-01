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
from app.repository import KeyRepository


class Key:
    """Key Class"""

    def __init__(self):
        self.key = KeyRepository()
        self.logger = Logger().get_logger(__name__)

    def get_one_by_id(self, id):
        """
        Get a Key by ID
        """
        return self.key.get_one_by_id(id)

    def create(self, data):
        """
        Create a Key
        """
        result = self.key.insert_one(data)

        if request:
            self.logger.info(
                "Create an ssh key with id {} and name {}".format(
                    result.id, result.name
                )
            )

        return result

    def update(self, id, data):
        """
        Update a Key By ID
        """
        self.logger.info("Update an ssh key with id {}".format(id))

        return self.key.update_one_by_id(id, data)

    def delete_by_id(self, id):
        """
        Delete a Key By ID
        """
        self.logger.info("Delete an ssh key with id {}".format(id))

        return self.key.delete_one_by_id(id)
