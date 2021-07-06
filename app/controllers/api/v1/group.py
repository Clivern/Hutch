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
from app.repository import GroupRepository
from app.controllers.controller import Controller


class GetGroup(View, Controller):
    """GetGroup Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, group_id):
        """
        Get Group
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class GetGroups(View, Controller):
    """GetGroups Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Get Groups
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class CreateGroup(View, Controller):
    """CreateGroup Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create Group
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class UpdateGroup(View, Controller):
    """UpdateGroup Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def put(self, request, group_id):
        """
        Update Group
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class DeleteGroup(View, Controller):
    """DeleteGroup Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = GroupRepository()
        self.logger = Logger().get_logger(__name__)

    def delete(self, request, group_id):
        """
        Delete Group
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)
