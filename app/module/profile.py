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
from app.repository.profile_repository import ProfileRepository
from app.repository.user_repository import UserRepository


class Profile:
    """Profile Class"""

    def __init__(self):
        self.logger = Logger().get_logger(__name__)
        self.profile_repository = ProfileRepository()
        self.user_repository = UserRepository()

    def get_profile(self, user_id):
        """
        Get Profile by User ID
        """
        return self.profile_repository.get_profile_by_user_id(user_id)

    def get_user(self, user_id):
        """
        Get User By ID
        """
        return self.user_repository.get_one_by_id(user_id)

    def update_profile_by_user_id(self, user_id, data):
        """
        Update Profile by User ID
        """
        return self.profile_repository.update_profile(data.update({"user": user_id}))

    def update_user_by_id(self, user_id, data):
        """
        Update User By ID
        """
        return self.user_repository.update_one_by_id(user_id, data)
