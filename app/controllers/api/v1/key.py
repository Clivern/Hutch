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
from app.module.key import Key as KeyModule
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.exceptions.invalid_request import InvalidRequest


class GetKey(View, Controller):
    """GetKey Endpoint Controller"""

    def __init__(self):
        self.key = KeyModule()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, key_id):
        """
        Get Key
        """
        self.logger.info("Validate incoming request")

        return JsonResponse({}, status=HTTPStatus.OK)


class GetKeys(View, Controller):
    """GetKeys Endpoint Controller"""

    def __init__(self):
        self.key = KeyModule()
        self.validator = Validator()
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
        self.key = KeyModule()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create Key
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/create_key.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        return JsonResponse({}, status=HTTPStatus.OK)


class UpdateKey(View, Controller):
    """UpdateKey Endpoint Controller"""

    def __init__(self):
        self.key = KeyModule()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def put(self, request, key_id):
        """
        Update Key
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/update_key.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        return JsonResponse({}, status=HTTPStatus.OK)


class DeleteKey(View, Controller):
    """DeleteKey Endpoint Controller"""

    def __init__(self):
        self.key = KeyModule()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    def delete(self, request, key_id):
        """
        Delete Key
        """
        self.logger.info("Validate incoming request")

        self.logger.info("Incoming request is valid")

        self.logger.info("Delete ssh key with id {}".format(key_id))

        self.key.delete_by_id(key_id)

        self.logger.info("SSH key with id {} got deleted".format(key_id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)
