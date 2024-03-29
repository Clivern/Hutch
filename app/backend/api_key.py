# Copyright 2022 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from app.repository import ProfileRepository

from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend


class ApiKeyBackend(BaseBackend):
    """API Key Backend"""

    def authenticate(self, request, api_key=None):
        try:
            repository = ProfileRepository()

            user = repository.get_user_by_api_key(api_key)

            if user:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
