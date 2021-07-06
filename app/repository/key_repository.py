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

from slugify import slugify
from django.contrib.auth.models import User
from app.models import Key


class KeyRepository:
    """Key Repository"""

    def insert_one(self, data):
        """
        Insert ssh key
        """
        key = Key()

        if "name" in data:
            key.name = data["name"]

        if "slug" in data:
            key.slug = data["slug"]
        else:
            key.slug = slugify(data["name"])

        if "remote_id" in data:
            key.remote_id = data["remote_id"]

        if "cloud_provider" in data:
            key.cloud_provider = data["cloud_provider"]

        if "uuid" in data:
            key.uuid = data["uuid"]
        else:
            key.uuid = str(uuid.uuid4())

        if "public_key" in data:
            key.public_key = data["public_key"]

        if "private_key" in data:
            key.private_key = data["private_key"]

        if "user_id" in data:
            key.user = User.objects.get(pk=data["user_id"])

        key.save()
        return False if key.pk is None else key

    def update_one_by_id(self, id, data):
        """
        Update ssh key by id
        """
        key = self.get_one_by_id(id)

        if key is not False:
            if "name" in data:
                key.name = data["name"]

            if "slug" in data:
                key.slug = data["slug"]

            if "remote_id" in data:
                key.remote_id = data["remote_id"]

            if "cloud_provider" in data:
                key.cloud_provider = data["cloud_provider"]

            if "public_key" in data:
                key.public_key = data["public_key"]

            if "private_key" in data:
                key.private_key = data["private_key"]

            if "user_id" in data:
                key.user = User.objects.get(pk=data["user_id"])

            key.save()
            return True
        return False

    def count_all(self):
        """
        Count all ssh keys
        """
        return Key.objects.count()

    def count_by_user(self, user_id=None):
        """
        Count ssh keys by  a user
        """
        if user_id is None:
            return Key.objects.count()
        else:
            return Key.objects.filter(user_id=user_id).count()

    def get_all(self, offset=None, limit=None):
        """
        Get all ssh keys
        """
        if offset is None or limit is None:
            return Key.objects.order_by("-created_at")

        return Key.objects.order_by("-created_at")[offset : limit + offset]

    def get(self, user_id, offset=None, limit=None):
        """
        Get ssh keys by user id
        """
        if offset is None or limit is None:
            return Key.objects.filter(user_id=user_id).order_by("-created_at")

        return Key.objects.filter(user_id=user_id).order_by("-created_at")[
            offset : limit + offset
        ]

    def get_one_by_id(self, id):
        """
        Get ssh key by id
        """
        try:
            key = Key.objects.get(id=id)
            return False if key.pk is None else key
        except Exception:
            return False

    def delete_one_by_id(self, id):
        """
        Delete ssh key by id
        """
        key = self.get_one_by_id(id)

        if key is not False:
            count, deleted = key.delete()
            return True if count > 0 else False

        return False
