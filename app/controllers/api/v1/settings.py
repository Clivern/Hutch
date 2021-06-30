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
from app.util.validator import Validator
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.module.settings import Settings as SettingsModule
from app.exceptions.invalid_request import InvalidRequest
from app.helpers.decorators import prevent_if_not_authenticated


class Settings(View, Controller):
    """Settings Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.settings = SettingsModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def post(self, request):
        """
        Settings Request
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/settings.json"),
        )

        if not result:
            self.logger.info(
                "Request is invalid: {}".format(self.validator.get_error())
            )

            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Update settings")

        self.settings.update_settings(
            {
                "app_name": data["app_name"],
                "app_url": data["app_url"],
                "app_email": data["app_email"],
                "digitalocean_status": data["digitalocean_status"],
                "digitalocean_api_token": data["digitalocean_api_token"],
            }
        )

        return JsonResponse(
            {"successMessage": _("Settings updated successfully!")},
            status=HTTPStatus.OK,
        )
