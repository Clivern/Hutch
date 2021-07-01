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

from app.service.ssh import SSH
from app.shortcuts import Logger
from app.util.validator import Validator
from app.module.key import Key as KeyModule
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.exceptions.invalid_request import InvalidRequest
from app.exceptions.resource_not_found import ResourceNotFound
from app.helpers.decorators import prevent_if_not_authenticated


class Key(View, Controller):
    """Key Endpoint Controller"""

    def __init__(self):
        self.key = KeyModule()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request, key_id):
        """
        Get Key
        """
        self.logger.info("Validate incoming request")

        key = self.key.get_one_by_id(key_id, request.user.id)

        if not key:
            self.logger.info("Key with id {} not found".format(key_id))
            raise ResourceNotFound("Key with id {} not found".format(key_id))

        return JsonResponse(
            {
                "id": key.id,
                "uuid": key.uuid,
                "name": key.name,
                "slug": key.slug,
                "cloudProvider": key.cloud_provider,
                "remoteId": key.remote_id,
                "user": {"id": key.user.id, "email": key.user.email},
                "publicKey": key.public_key,
                "privateKey": key.private_key,
                "hostsCount": self.key.count_hosts_by_key(key.id, request.user.id),
                "createdAt": key.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": key.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )

    @prevent_if_not_authenticated
    def delete(self, request, key_id):
        """
        Delete Key
        """
        self.logger.info("Validate incoming request")

        if self.key.count_hosts_by_key(key_id, request.user.id) > 0:
            raise InvalidRequest(_("SSH Key is attached to a host"))

        self.logger.info("Incoming request is valid")

        self.logger.info("Delete ssh key with id {}".format(key_id))

        self.key.delete_by_id(key_id, request.user.id)

        self.logger.info("SSH key with id {} got deleted".format(key_id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)


class Keys(View, Controller):
    """Keys Endpoint Controller"""

    def __init__(self):
        self.key = KeyModule()
        self.validator = Validator()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request):
        """
        Get Keys
        """
        try:
            offset = int(request.GET["offset"])
            limit = int(request.GET["limit"])
        except Exception:
            offset = 0
            limit = 20

        result = []
        keys = self.key.get_user_keys(request.user.id, offset, limit)

        for key in keys:
            result.append(
                {
                    "id": key.id,
                    "uuid": key.uuid,
                    "name": key.name,
                    "slug": key.slug,
                    "cloudProvider": key.cloud_provider,
                    "remoteId": key.remote_id,
                    "user": {"id": key.user.id, "email": key.user.email},
                    "publicKey": key.public_key,
                    "privateKey": key.private_key,
                    "hostsCount": self.key.count_hosts_by_key(key.id, request.user.id),
                    "createdAt": key.created_at.strftime("%b %d %Y %H:%M:%S"),
                    "updatedAt": key.updated_at.strftime("%b %d %Y %H:%M:%S"),
                }
            )

        return JsonResponse(
            {
                "keys": result,
                "_metadata": {
                    "limit": limit,
                    "offset": offset,
                    "totalCount": self.key.count_user_keys(request.user.id),
                },
            }
        )

    @prevent_if_not_authenticated
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

        key = self.key.create(
            {
                "name": data["name"],
                "cloud_provider": data["cloudProvider"],
                "public_key": data["publicKey"],
                "private_key": data["privateKey"],
                "user_id": request.user.id,
            }
        )

        return JsonResponse(
            {
                "id": key.id,
                "uuid": key.uuid,
                "name": key.name,
                "slug": key.slug,
                "cloudProvider": key.cloud_provider,
                "remoteId": key.remote_id,
                "user": {"id": key.user.id, "email": key.user.email},
                "publicKey": key.public_key,
                "privateKey": key.private_key,
                "hostsCount": self.key.count_hosts_by_key(key.id, request.user.id),
                "createdAt": key.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": key.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.CREATED,
        )


class GenerateKey(View, Controller):
    """GenerateKey Endpoint Controller"""

    def __init__(self):
        self.ssh = SSH()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request):
        """
        Generate a Key
        """
        self.logger.info("Validate incoming request")

        self.logger.info("Incoming request is valid")

        result = self.ssh.generate()

        return JsonResponse(
            {"privateKey": result["private_key"], "publicKey": result["public_key"]},
            status=HTTPStatus.OK,
        )
