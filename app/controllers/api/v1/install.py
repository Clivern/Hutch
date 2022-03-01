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
from app.exceptions.invalid_request import InvalidRequest


class Install(View, Controller):
    """Install Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Install Request

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode('utf-8'),
            self.validator.get_schema_path("/schemas/api/v1/install.json")
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        return JsonResponse({}, status=HTTPStatus.OK)
