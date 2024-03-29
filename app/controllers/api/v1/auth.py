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

import json
from http import HTTPStatus

from django.views import View
from django.http import JsonResponse

from app.shortcuts import Logger
from app.module.auth import Auth
from app.util.validator import Validator
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.exceptions.invalid_request import InvalidRequest


class Login(View, Controller):
    """Login Endpoint Controller"""

    def __init__(self):
        self.auth = Auth()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Login Request
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/login.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        result = self.auth.authenticate(data["email"], data["password"], request)

        if result:
            return JsonResponse(
                {"successMessage": _("User logged in successfully!")},
                status=HTTPStatus.ACCEPTED,
            )
        else:
            return JsonResponse(
                {"errorMessage": _("Invalid username or password!")},
                status=HTTPStatus.FORBIDDEN,
            )


class ForgotPassword(View, Controller):
    """ForgotPassword Endpoint Controller"""

    def __init__(self):
        self.auth = Auth()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Forgot Password Request
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/forgot_password.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        return JsonResponse({}, status=HTTPStatus.OK)


class ResetPassword(View, Controller):
    """ResetPassword Endpoint Controller"""

    def __init__(self):
        self.auth = Auth()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Reset Password Request
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/reset_password.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        return JsonResponse({}, status=HTTPStatus.OK)
