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
from app.module.cluster import Cluster as ClusterModule
from django.utils.translation import gettext as _
from app.controllers.controller import Controller
from app.exceptions.invalid_request import InvalidRequest
from app.exceptions.resource_not_found import ResourceNotFound
from app.helpers.decorators import prevent_if_not_authenticated


class Clusters(View, Controller):
    """Clusters Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.cluster = ClusterModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request):
        """
        Get Clusters
        """
        try:
            offset = int(request.GET["offset"])
            limit = int(request.GET["limit"])
        except Exception:
            offset = 0
            limit = 20

        result = []
        clusters = self.cluster.get_user_clusters(request.user.id, offset, limit)

        for cluster in clusters:
            result.append(
                {
                    "id": cluster.id,
                    "uuid": cluster.uuid,
                    "name": cluster.name,
                    "description": cluster.description,
                    "status": cluster.status,
                    "cloudProvider": cluster.cloud_provider,
                    "specification": json.loads(cluster.specification),
                    "user": {"id": cluster.user.id, "email": cluster.user.email},
                    "group": {
                        "id": cluster.group.id,
                        "name": cluster.group.name,
                        "uuid": cluster.group.uuid,
                    },
                    "key": {
                        "id": cluster.key.id,
                        "name": cluster.key.name,
                        "uuid": cluster.key.uuid,
                    },
                    "hostsCount": self.cluster.count_hosts_by_cluster(
                        cluster_id, request.user.id
                    ),
                    "createdAt": cluster.created_at.strftime("%b %d %Y %H:%M:%S"),
                    "updatedAt": cluster.updated_at.strftime("%b %d %Y %H:%M:%S"),
                }
            )

        return JsonResponse(
            {
                "clusters": result,
                "_metadata": {
                    "limit": limit,
                    "offset": offset,
                    "totalCount": self.cluster.count_user_clusters(request.user.id),
                },
            }
        )

    @prevent_if_not_authenticated
    def post(self, request):
        """
        Create cluster
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/create_cluster.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        cluster = self.cluster.create(
            {
                "name": data["name"],
                "description": data["description"],
                "user_id": request.user.id,
                "cloud_provider": data["cloudProvider"],
                "specification": json.dumps(data["specification"]),
                "group_id": data["group_id"],
                "key_id": data["key_id"],
            }
        )

        return JsonResponse(
            {
                "id": cluster.id,
                "uuid": cluster.uuid,
                "name": cluster.name,
                "description": cluster.description,
                "status": cluster.status,
                "cloudProvider": cluster.cloud_provider,
                "specification": json.loads(cluster.specification),
                "user": {"id": cluster.user.id, "email": cluster.user.email},
                "group": {
                    "id": cluster.group.id,
                    "name": cluster.group.name,
                    "uuid": cluster.group.uuid,
                },
                "key": {
                    "id": cluster.key.id,
                    "name": cluster.key.name,
                    "uuid": cluster.key.uuid,
                },
                "hostsCount": self.cluster.count_hosts_by_cluster(
                    cluster_id, request.user.id
                ),
                "createdAt": cluster.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": cluster.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.CREATED,
        )


class Cluster(View, Controller):
    """Cluster Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.cluster = ClusterModule()
        self.logger = Logger().get_logger(__name__)

    @prevent_if_not_authenticated
    def get(self, request, cluster_id):
        """
        Get Cluster
        """
        self.logger.info("Validate incoming request")

        cluster = self.cluster.get_one_by_id(cluster_id, request.user.id)

        if not cluster:
            self.logger.info("Cluster with id {} not found".format(cluster_id))
            raise ResourceNotFound("Cluster with id {} not found".format(cluster_id))

        return JsonResponse(
            {
                "id": cluster.id,
                "uuid": cluster.uuid,
                "name": cluster.name,
                "description": cluster.description,
                "status": cluster.status,
                "cloudProvider": cluster.cloud_provider,
                "specification": json.loads(cluster.specification),
                "user": {"id": cluster.user.id, "email": cluster.user.email},
                "group": {
                    "id": cluster.group.id,
                    "name": cluster.group.name,
                    "uuid": cluster.group.uuid,
                },
                "key": {
                    "id": cluster.key.id,
                    "name": cluster.key.name,
                    "uuid": cluster.key.uuid,
                },
                "hostsCount": self.cluster.count_hosts_by_cluster(
                    cluster_id, request.user.id
                ),
                "createdAt": cluster.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": cluster.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )

    @prevent_if_not_authenticated
    def put(self, request, cluster_id):
        """
        Update Cluster
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode("utf-8"),
            self.validator.get_schema_path("/schemas/api/v1/update_cluster.json"),
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        cluster = self.cluster.get_one_by_id(cluster_id, request.user.id)

        if not cluster:
            self.logger.info("Cluster with id {} not found".format(cluster_id))
            raise ResourceNotFound("Cluster with id {} not found".format(cluster_id))

        data = json.loads(request.body.decode("utf-8"))

        self.logger.info("Incoming request is valid")

        self.cluster.update(
            cluster_id,
            {
                "name": data["name"],
                "description": data["description"],
                "user_id": request.user.id,
                "cloud_provider": data["cloudProvider"],
                "specification": json.dumps(data["specification"]),
                "group_id": data["group_id"],
                "key_id": data["key_id"],
            },
        )

        cluster = self.cluster.get_one_by_id(cluster_id, request.user.id)

        return JsonResponse(
            {
                "id": cluster.id,
                "uuid": cluster.uuid,
                "name": cluster.name,
                "description": cluster.description,
                "status": cluster.status,
                "cloudProvider": cluster.cloud_provider,
                "specification": json.loads(cluster.specification),
                "user": {"id": cluster.user.id, "email": cluster.user.email},
                "group": {
                    "id": cluster.group.id,
                    "name": cluster.group.name,
                    "uuid": cluster.group.uuid,
                },
                "key": {
                    "id": cluster.key.id,
                    "name": cluster.key.name,
                    "uuid": cluster.key.uuid,
                },
                "hostsCount": self.cluster.count_hosts_by_cluster(
                    cluster_id, request.user.id
                ),
                "createdAt": cluster.created_at.strftime("%b %d %Y %H:%M:%S"),
                "updatedAt": cluster.updated_at.strftime("%b %d %Y %H:%M:%S"),
            },
            status=HTTPStatus.OK,
        )

    @prevent_if_not_authenticated
    def delete(self, request, cluster_id):
        """
        Delete Cluster
        """
        self.logger.info("Validate incoming request")

        self.logger.info("Incoming request is valid")

        self.logger.info("Delete cluster with id {}".format(cluster_id))

        self.cluster.delete_by_id(cluster_id, request.user.id)

        self.logger.info("Cluster with id {} got deleted".format(cluster_id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)
