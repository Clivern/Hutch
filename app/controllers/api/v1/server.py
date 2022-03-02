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
from app.controllers.controller import Controller


class GetServer(View, Controller):
    """GetServer Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, server_id):
        """
        Get Server Request

        Args:
            request: the request
            server_id: The server id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class GetServers(View, Controller):
    """GetServers Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Get Server Request

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class CreateServer(View, Controller):
    """CreateServer Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create Server Request

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class UpdateServer(View, Controller):
    """UpdateServer Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def put(self, request, server_id):
        """
        Update Server Request

        Args:
            request: the request
            server_id: The server id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class DeleteServer(View, Controller):
    """DeleteServer Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def delete(self, request, server_id):
        """
        Delete Server Request

        Args:
            request: the request
            server_id: The server id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class TriggerServerPlan(View, Controller):
    """TriggerServerPlan Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request, server_id, plan_id):
        """
        Trigger Server Plan

        Args:
            request: the request
            server_id: The server id
            plan_id: The plan id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)
