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
from app.module.host import Host as HostModule
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.exceptions.invalid_request import InvalidRequest
from app.exceptions.resource_not_found import ResourceNotFound
from app.helpers.decorators import prevent_if_not_authenticated


class Hosts(View, Controller):
    """Hosts Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host = HostModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request):
        """
        Get Hosts
        """
        try:
            offset = int(request.GET["offset"])
            limit = int(request.GET["limit"])
        except Exception:
            offset = 0
            limit = 20

        result = []
        hosts = self.host.get_user_hosts(request.user.id, offset, limit)

        for host in hosts:
            result.append(
                {
                    "id": host.id,
                    "uuid": host.uuid,
                    "createdAt": host.created_at.strftime("%b %d %Y %H:%M:%S"),
                    "updatedAt": host.updated_at.strftime("%b %d %Y %H:%M:%S"),
                }
            )

        return JsonResponse(
            {
                "hosts": result,
                "_metadata": {
                    "limit": limit,
                    "offset": offset,
                    "totalCount": self.host.count_user_hosts(request.user.id),
                },
            }
        )

    @prevent_if_not_authenticated
    def post(self, request):
        """
        Create Host
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/create_host.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        host = self.host.create(
            {
                "name": data["name"],
                "description": data["description"],
                "user_id": request.user.id,
            }
        )

        return JsonResponse(
            {
                "id": host.id,
                "uuid": host.uuid,
                "createdAt": host.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": host.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.CREATED,
        )


class Host(View, Controller):
    """Host Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.host = HostModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request, host_id):
        """
        Get Host
        """
        self.logger.info("Validate incoming request")

        host = self.host.get_one_by_id(host_id, request.user.id)

        if not host:
            self.logger.info("Host with id {} not found".format(host_id))
            raise ResourceNotFound("Host with id {} not found".format(host_id))

        return JsonResponse(
            {
                "id": host.id,
                "uuid": host.uuid,
                "createdAt": host.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": host.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )

    @prevent_if_not_authenticated
    def put(self, request, host_id):
        """
        Update Host
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/update_host.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        host = self.host.get_one_by_id(host_id, request.user.id)

        if not host:
            self.logger.info("Host with id {} not found".format(host_id))
            raise ResourceNotFound("Host with id {} not found".format(host_id))

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        self.host.update(
            host_id,
            {
                "name": data["name"],
                "description": data["description"],
            },
        )

        host = self.host.get_one_by_id(host_id, request.user.id)

        return JsonResponse(
            {
                "id": host.id,
                "uuid": host.uuid,
                "createdAt": host.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": host.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )

    @prevent_if_not_authenticated
    def delete(self, request, host_id):
        """
        Delete Host
        """
        self.logger.info("Validate incoming request")

        self.logger.info("Incoming request is valid")

        self.logger.info("Delete host with id {}".format(host_id))

        self.host.delete_by_id(host_id, request.user.id)

        self.logger.info("Host with id {} got deleted".format(host_id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)
