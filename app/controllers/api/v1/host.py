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
from app.repository import HostRepository
from app.controllers.controller import Controller


class GetHost(View, Controller):
    """GetHost Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, host_id):
        """
        Get Host Request

        Args:
            request: the request
            host_id: The host id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class GetHosts(View, Controller):
    """GetHosts Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Get Host Request

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class CreateHost(View, Controller):
    """CreateHost Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create Host Request

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class UpdateHost(View, Controller):
    """UpdateHost Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def put(self, request, host_id):
        """
        Update Host Request

        Args:
            request: the request
            host_id: The host id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class DeleteHost(View, Controller):
    """DeleteHost Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def delete(self, request, host_id):
        """
        Delete Host Request

        Args:
            request: the request
            host_id: The host id

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class TriggerHostPlan(View, Controller):
    """TriggerHostPlan Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request, host_id, plan_id):
        """
        Trigger Host Plan
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)
