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

import uuid

from app.shortcuts import Logger
from app.repository.option_repository import OptionRepository
from app.repository.user_repository import UserRepository
from app.repository.profile_repository import ProfileRepository


class Install:
    """Install Class"""

    def __init__(self):
        self.logger = Logger().get_logger(__name__)
        self.option_repository = OptionRepository()
        self.user_repository = UserRepository()
        self.profile_repository = ProfileRepository()

    def is_installed(self):
        """
        Check if the application is installed
        """
        return (
            False
            if self.option_repository.get_one_by_name("app_installed") is False
            else True
        )

    def install(self, app_data, admin_data):
        """
        Install the application
        """
        # Create a User
        user = self.user_repository.insert_one(
            {
                "first_name": admin_data["first_name"],
                "last_name": admin_data["last_name"],
                "email": admin_data["email"],
                "password": admin_data["password"],
                "is_superuser": True,
                "is_staff": True,
            }
        )

        # Create a Profile
        self.profile_repository.create_profile(
            {
                "job_title": "",
                "company": "",
                "personal_url": "",
                "api_key": str(uuid.uuid4()),
                "user": user.pk,
            }
        )

        # Store app data
        self.option_repository.insert_many(
            [
                {"name": "app_name", "value": app_data["app_name"], "autoload": True},
                {"name": "app_email", "value": app_data["app_email"], "autoload": True},
                {"name": "app_url", "value": app_data["app_url"], "autoload": True},
                {"name": "app_installed", "value": "true", "autoload": False},
                {"name": "digitalocean_status", "value": "disabled", "autoload": False},
                {"name": "digitalocean_api_token", "value": "", "autoload": False},
            ]
        )
