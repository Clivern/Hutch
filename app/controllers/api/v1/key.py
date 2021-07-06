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
from app.repository import KeyRepository
from app.controllers.controller import Controller


class GetKey(View, Controller):
    """GetKey Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = KeyRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, host_id):
        """
        Get Key
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class GetKeys(View, Controller):
    """GetKeys Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = KeyRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Get Keys
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class CreateKey(View, Controller):
    """CreateKey Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = KeyRepository()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create Key
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class UpdateKey(View, Controller):
    """UpdateKey Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = KeyRepository()
        self.logger = Logger().get_logger(__name__)

    def put(self, request, host_id):
        """
        Update Key
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class DeleteKey(View, Controller):
    """DeleteKey Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host_repository = KeyRepository()
        self.logger = Logger().get_logger(__name__)

    def delete(self, request, host_id):
        """
        Delete Key
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)
