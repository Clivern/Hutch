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

from django.contrib.auth.models import User

from app.models import Key
from app.models import Group
from app.models import Host
from app.models import Cluster
from app.models import ClusterMeta


class ClusterRepository:
    """Cluster Repository"""

    def insert_one(self, data):
        """
        Insert a new cluster
        """
        cluster = Cluster()

        if "name" in data:
            cluster.name = data["name"]

        if "uuid" in data:
            cluster.uuid = data["uuid"]
        else:
            cluster.uuid = str(uuid.uuid4())

        if "description" in data:
            cluster.description = data["description"]

        if "cloud_provider" in data:
            cluster.cloud_provider = data["cloud_provider"]

        if "specification" in data:
            cluster.specification = data["specification"]

        if "status" in data:
            cluster.status = data["status"]

        if "user_id" in data:
            cluster.user = User.objects.get(pk=data["user_id"])

        if "key_id" in data:
            cluster.key = Key.objects.get(pk=data["key_id"])

        if "group_id" in data:
            cluster.group = Group.objects.get(pk=data["group_id"])

        cluster.save()

        return False if cluster.pk is None else cluster

    def update_one_by_id(self, id, data):
        """
        Update cluster by id
        """
        cluster = Cluster.objects.get(id=id)

        if cluster is not False:
            if "name" in data:
                cluster.name = data["name"]

            if "uuid" in data:
                cluster.uuid = data["uuid"]

            if "description" in data:
                cluster.description = data["description"]

            if "cloud_provider" in data:
                cluster.cloud_provider = data["cloud_provider"]

            if "specification" in data:
                cluster.specification = data["specification"]

            if "status" in data:
                cluster.status = data["status"]

            if "user_id" in data:
                cluster.user = User.objects.get(pk=data["user_id"])

            if "key_id" in data:
                cluster.key = Key.objects.get(pk=data["key_id"])

            if "group_id" in data:
                cluster.group = Group.objects.get(pk=data["group_id"])

            cluster.save()
            return True

        return False

    def count_all(self):
        """
        Count all clusters
        """
        return Cluster.objects.count()

    def count_by_user(self, user_id=None):
        """
        Count clusters by user id
        """
        if user_id is None:
            return Cluster.objects.count()
        else:
            return Cluster.objects.filter(user_id=user_id).count()

    def count_hosts_by_cluster(self, cluster_id=None, user_id=None):
        """
        Count hosts by cluster id
        """
        if cluster_id is None:
            return Host.objects.count()
        else:
            return Host.objects.filter(cluster_id=cluster_id, user_id=user_id).count()

    def get_all(self, offset=None, limit=None):
        """
        Get all clusters
        """
        if offset is None or limit is None:
            return Cluster.objects.order_by("-created_at")

        return Cluster.objects.order_by("-created_at")[offset : limit + offset]

    def get(self, user_id, offset=None, limit=None):
        """
        Get clusters by user id
        """
        if offset is None or limit is None:
            return Cluster.objects.filter(user_id=user_id).order_by("-created_at")

        return Cluster.objects.filter(user_id=user_id).order_by("-created_at")[
            offset : limit + offset
        ]

    def get_one_by_id(self, id, user_id):
        """
        Get cluster by id
        """
        try:
            cluster = Cluster.objects.get(id=id, user_id=user_id)
            return False if cluster.pk is None else cluster
        except Exception:
            return False

    def delete_one_by_id(self, id, user_id):
        """
        Delete cluster by id
        """
        cluster = self.get_one_by_id(id, user_id)

        if cluster is not False:
            count, deleted = cluster.delete()
            return True if count > 0 else False

        return False

    def add_meta(self, cluster_id, name, value):
        """
        Add Cluster Meta
        """
        meta = ClusterMeta()

        meta.host = Cluster.objects.get(pk=cluster_id)
        meta.name = name
        meta.value = value

        meta.save()

        return False if meta.pk is None else meta

    def get_cluster_meta(self, cluster_id, name):
        """
        Get Cluster Meta
        """
        meta = ClusterMeta.objects.filter(cluster_id=cluster_id, name=name).first()

        if meta is None or meta.pk is None:
            return None

        return meta

    def delete_cluster_meta(self, cluster_id, name):
        """
        Delete Cluster Meta
        """
        meta = self.get_cluster_meta(cluster_id, name)

        if meta is not False:
            count, deleted = meta.delete()
            return True if count > 0 else False

        return False
