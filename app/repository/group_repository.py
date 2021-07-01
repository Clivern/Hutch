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

from app.models import Group
from app.models import Host


class GroupRepository:
    """Group Repository"""

    def insert_one(self, data):
        """
        Insert a new group
        """
        group = Group()

        if "name" in data:
            group.name = data["name"]

        if "uuid" in data:
            group.uuid = data["uuid"]
        else:
            group.uuid = str(uuid.uuid4())

        if "description" in data:
            group.description = data["description"]

        if "user_id" in data:
            group.user = User.objects.get(pk=data["user_id"])

        group.save()
        return False if group.pk is None else group

    def update_one_by_id(self, id, data):
        """
        Update a group by id
        """
        group = self.get_one_by_id(id)

        if group is not False:
            if "name" in data:
                group.name = data["name"]

            if "description" in data:
                group.description = data["description"]

            group.save()
            return True
        return False

    def count_all(self):
        """
        Count all groups
        """
        return Group.objects.count()

    def count_by_user(self, user_id=None):
        """
        Count groups by user id
        """
        if user_id is None:
            return Group.objects.count()
        else:
            return Group.objects.filter(user_id=user_id).count()

    def count_hosts_by_group(self, group_id=None, user_id=None):
        """
        Count hosts by group id
        """
        if group_id is None:
            return Host.objects.count()
        else:
            return Host.objects.filter(group_id=group_id, user_id=user_id).count()

    def get_all(self, offset=None, limit=None):
        """
        Get all groups
        """
        if offset is None or limit is None:
            return Group.objects.order_by("-created_at")

        return Group.objects.order_by("-created_at")[offset : limit + offset]

    def get(self, user_id, offset=None, limit=None):
        """
        Get groups by user id
        """
        if offset is None or limit is None:
            return Group.objects.filter(user_id=user_id).order_by("-created_at")

        return Group.objects.filter(user_id=user_id).order_by("-created_at")[
            offset : limit + offset
        ]

    def get_one_by_id(self, id, user_id):
        """
        Get a group by id
        """
        try:
            group = Group.objects.get(id=id, user_id=user_id)
            return False if group.pk is None else group
        except Exception:
            return False

    def delete_one_by_id(self, id, user_id):
        """
        Delete a group by id
        """
        group = self.get_one_by_id(id, user_id)

        if group is not False:
            count, deleted = group.delete()
            return True if count > 0 else False

        return False
