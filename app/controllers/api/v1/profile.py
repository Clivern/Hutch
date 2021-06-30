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
import json
from http import HTTPStatus

from django.views import View
from django.http import JsonResponse

from app.shortcuts import Logger
from app.util.validator import Validator
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.module.profile import Profile as ProfileModule
from app.exceptions.invalid_request import InvalidRequest
from app.helpers.decorators import prevent_if_not_authenticated


class Profile(View, Controller):
    """Profile Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.profile = ProfileModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def post(self, request):
        """
        Profile Request
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/profile.json"),
        )

        if not result:
            self.logger.info(
                "Request is invalid: {}".format(self.validator.get_error())
            )

            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.profile.update_profile_by_user_id(
            request.user.id,
            {
                "theme": data["theme"],
                "company": data["company"],
                "team": data["team"],
                "job_title": data["job_title"],
                "personal_url": data["personal_url"],
            },
        )

        self.profile.update_user_by_id(
            request.user.id,
            {
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "email": data["email"],
            },
        )

        return JsonResponse(
            {"successMessage": _("Profile updated successfully!")},
            status=HTTPStatus.OK,
        )


class Access(View, Controller):
    """Access Endpoint Controller"""

    def __init__(self):
        self.profile = ProfileModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def post(self, request):
        """
        API Access Request
        """
        self.logger.info("Validate incoming request")

        self.profile.update_profile_by_user_id(
            request.user.id, {"api_key": str(uuid.uuid4())}
        )

        return JsonResponse(
            {"successMessage": _("API key updated successfully!")},
            status=HTTPStatus.OK,
        )
