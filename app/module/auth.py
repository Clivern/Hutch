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

from django.core.validators import validate_email
from django.contrib.auth import authenticate, login

from app.shortcuts import Logger
from app.repository.user_repository import UserRepository


class Auth:
    """Auth Class"""

    def __init__(self):
        self.user_repository = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def is_authenticated(self, request):
        """
        Check if user is authenticated
        """
        if request.user and request.user.is_authenticated:
            return True
        else:
            return False

    def authenticate(self, email, password, request=None, with_login=True):
        """
        Authenticate with email
        """
        is_email = False

        try:
            is_email = True if validate_email(email) is None else False
        except Exception:
            is_email = False

        if is_email:
            user = self.user_repository.get_one_by_email(email)
            if user is not False and user.check_password(password) is True:
                if with_login:
                    self.__login(request, user)
                return True
            else:
                return False
        else:
            return False

    def __login(self, request, user):
        """
        Login into the app
        """
        return login(request, user)
