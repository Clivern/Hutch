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

from django.contrib.auth.models import User
from app.models import Group
from app.models import Key


class HostRepository:
    """Host Repository"""

    def insert_one(self, data):
        """
        Insert a host
        """
        host = Host()

        if "name" in data:
            host.name = data["name"]

        if "uuid" in data:
            host.uuid = data["uuid"]

        if "cloud_provider" in data:
            host.cloud_provider = data["cloud_provider"]

        if "specification" in data:
            host.specification = data["specification"]

        if "hostname" in data:
            host.hostname = data["hostname"]

        if "username" in data:
            host.username = data["username"]

        if "ipaddress" in data:
            host.ipaddress = data["ipaddress"]

        if "user_id" in data:
            host.user = User.objects.get(pk=data["user_id"])

        if "key_id" in data:
            host.key = Key.objects.get(pk=data["key_id"])

        if "group_id" in data:
            host.group = Group.objects.get(pk=data["group_id"])

        host.save()
        return False if host.pk is None else host

    def update_one_by_id(self, id, data):
        """
        Update host by id
        """
        host = self.get_one_by_id(id)

        if host is not False:
            if "name" in data:
                host.name = data["name"]

            if "uuid" in data:
                host.uuid = data["uuid"]

            if "cloud_provider" in data:
                host.cloud_provider = data["cloud_provider"]

            if "specification" in data:
                host.specification = data["specification"]

            if "hostname" in data:
                host.hostname = data["hostname"]

            if "username" in data:
                host.username = data["username"]

            if "ipaddress" in data:
                host.ipaddress = data["ipaddress"]

            if "user_id" in data:
                host.user = User.objects.get(pk=data["user_id"])

            if "key_id" in data:
                host.key = Key.objects.get(pk=data["key_id"])

            if "group_id" in data:
                host.group = Group.objects.get(pk=data["group_id"])

            host.save()
            return True
        return False

    def count_all(self):
        """
        Count all hosts
        """
        return Host.objects.count()

    def count_by_user(self, user_id=None):
        """
        Count hosts by user id
        """
        if user_id is None:
            return Host.objects.count()
        else:
            return Host.objects.filter(user_id=user_id).count()

    def get_all(self, offset=None, limit=None):
        """
        Get all hosts
        """
        if offset is None or limit is None:
            return Host.objects.order_by("-created_at")

        return Host.objects.order_by("-created_at")[offset : limit + offset]

    def get(self, user_id, offset=None, limit=None):
        """
        Get hosts by user id
        """
        if offset is None or limit is None:
            return Host.objects.filter(user_id=user_id).order_by("-created_at")

        return Host.objects.filter(user_id=user_id).order_by("-created_at")[
            offset : limit + offset
        ]

    def get_one_by_id(self, id):
        """
        Get host by id
        """
        try:
            activity = Host.objects.get(id=id)
            return False if activity.pk is None else activity
        except Exception:
            return False

    def delete_one_by_id(self, id):
        """
        Delete host by id
        """
        activity = self.get_one_by_id(id)

        if activity is not False:
            count, deleted = activity.delete()
            return True if count > 0 else False

        return False
