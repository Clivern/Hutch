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
from app.module.group import Group as GroupModule
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.exceptions.invalid_request import InvalidRequest
from app.exceptions.resource_not_found import ResourceNotFound
from app.helpers.decorators import prevent_if_not_authenticated


class GetGroup(View, Controller):
    """GetGroup Endpoint Controller"""

    def __init__(self):
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request, group_id):
        """
        Get Group
        """
        self.logger.info("Validate incoming request")

        group = self.group.get_one_by_id(group_id, request.user.id)

        if not group:
            self.logger.info("Group with id {} not found".format(group_id))
            raise ResourceNotFound("Group with id {} not found".format(group_id))

        return JsonResponse(
            {
                "id": group.id,
                "uuid": group.uuid,
                "name": group.name,
                "description": group.description,
                "user": {"id": group.user.id, "email": group.user.email},
                "createdAt": group.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": group.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )


class GetGroups(View, Controller):
    """GetGroups Endpoint Controller"""

    def __init__(self):
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request):
        """
        Get Groups
        """
        try:
            offset = int(request.GET["offset"])
            limit = int(request.GET["limit"])
        except Exception:
            offset = 0
            limit = 20

        result = []
        groups = self.group.get_user_groups(request.user.id, offset, limit)

        for group in groups:
            result.append(
                {
                    "id": group.id,
                    "uuid": group.uuid,
                    "name": group.name,
                    "description": group.description,
                    "user": {"id": group.user.id, "email": group.user.email},
                    "createdAt": group.created_at.strftime("%b %d %Y %H:%M:%S"),
                    "updatedAt": group.updated_at.strftime("%b %d %Y %H:%M:%S"),
                }
            )

        return JsonResponse(
            {
                "groups": result,
                "_metadata": {
                    "limit": limit,
                    "offset": offset,
                    "totalCount": self.group.count_user_groups(request.user.id),
                },
            }
        )


class CreateGroup(View, Controller):
    """CreateGroup Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def post(self, request):
        """
        Create Group
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/create_group.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        group = self.group.create(
            {
                "name": data["name"],
                "description": data["description"],
                "user_id": request.user.id,
            }
        )

        return JsonResponse(
            {
                "id": group.id,
                "uuid": group.uuid,
                "name": group.name,
                "description": group.description,
                "user": {"id": group.user.id, "email": group.user.email},
                "createdAt": group.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": group.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.CREATED,
        )


class UpdateGroup(View, Controller):
    """UpdateGroup Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def put(self, request, group_id):
        """
        Update Group
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/update_group.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        group = self.group.get_one_by_id(group_id, request.user.id)

        if not group:
            self.logger.info("Group with id {} not found".format(group_id))
            raise ResourceNotFound("Group with id {} not found".format(group_id))

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        self.group.update(
            group_id,
            {
                "name": data["name"],
                "description": data["description"],
            },
        )

        group = self.group.get_one_by_id(group_id, request.user.id)

        return JsonResponse(
            {
                "id": group.id,
                "uuid": group.uuid,
                "name": group.name,
                "description": group.description,
                "user": {"id": group.user.id, "email": group.user.email},
                "createdAt": group.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": group.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )


class DeleteGroup(View, Controller):
    """DeleteGroup Endpoint Controller"""

    def __init__(self):
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def delete(self, request, group_id):
        """
        Delete Group
        """
        self.logger.info("Validate incoming request")

        if self.group.count_hosts_by_group(group_id, request.user.id) > 0:
            raise InvalidRequest(_("SSH Key is attached to a host"))

        self.logger.info("Incoming request is valid")

        self.logger.info("Delete group with id {}".format(group_id))

        self.group.delete_by_id(group_id, request.user.id)

        self.logger.info("Group with id {} got deleted".format(group_id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)
