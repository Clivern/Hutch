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

from http import HTTPStatus

from django.views import View
from django.http import JsonResponse

from app.shortcuts import Logger
from app.util.validator import Validator
from app.repository import UserRepository
from app.controllers.controller import Controller


class GetUser(View, Controller):
    """GetUser Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.user_repository = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, user_id):
        """
        Get User
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class GetUsers(View, Controller):
    """GetUsers Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.user_repository = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Get Users
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class CreateUser(View, Controller):
    """CreateUser Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.user_repository = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create User
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class UpdateUser(View, Controller):
    """UpdateUser Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.user_repository = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def put(self, request, user_id):
        """
        Update User
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class DeleteUser(View, Controller):
    """DeleteUser Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.user_repository = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def delete(self, request, user_id):
        """
        Delete User
        """
        self.logger.info("Validate incoming request")

        self.user_repository.delete_one_by_id(int(user_id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)
