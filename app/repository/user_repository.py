# Copyright 2019 Silverbackhq
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserRepository:
    """User Repository"""

    def insert_one(self, user):
        """Insert a New User"""
        if self.get_one_by_email(user["email"]) is not False:
            return False

        new_user = User()

        if "username" in user:
            new_user.username = user["username"]
        else:
            new_user.username = str(uuid.uuid4())

        if "first_name" in user:
            new_user.first_name = user["first_name"]

        if "last_name" in user:
            new_user.last_name = user["last_name"]

        if "email" in user:
            new_user.email = user["email"]

        if "password" in user:
            new_user.password = make_password(user["password"])

        if "is_staff" in user:
            new_user.is_staff = user["is_staff"]

        if "is_active" in user:
            new_user.is_active = user["is_active"]

        if "is_superuser" in user:
            new_user.is_superuser = user["is_superuser"]

        if "last_login" in user:
            new_user.last_login = user["last_login"]

        if "date_joined" in user:
            new_user.date_joined = user["date_joined"]

        new_user.save()

        return False if new_user.pk is None else new_user

    def update_one_by_id(self, id, user_data):
        user = self.get_one_by_id(id)

        if user is not False:
            if "username" in user_data:
                user.username = user_data["username"]

            if "first_name" in user_data:
                user.first_name = user_data["first_name"]

            if "last_name" in user_data:
                user.last_name = user_data["last_name"]

            if "email" in user_data:
                user.email = user_data["email"]

            if "password" in user_data:
                user.password = make_password(user_data["password"])

            if "is_staff" in user_data:
                user.is_staff = user_data["is_staff"]

            if "is_active" in user_data:
                user.is_active = user_data["is_active"]

            if "is_superuser" in user_data:
                user.is_superuser = user_data["is_superuser"]

            if "last_login" in user_data:
                user.last_login = user_data["last_login"]

            if "date_joined" in user_data:
                user.date_joined = user_data["date_joined"]

            user.save()
            return True
        return False

    def get_one_by_id(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return False if user.pk is None else user
        except Exception:
            return False

    def get_one_by_email(self, email):
        """Get User By Email"""
        try:
            user = User.objects.get(email=email)
            return False if user.pk is None else user
        except Exception:
            return False

    def update_password_by_email(self, email, new_password):
        """Update Password by Email"""
        user = self.get_one_by_email(email)
        if user is not False:
            user.password = make_password(new_password)
            user.save()
            return True
        return False

    def validate_password_by_user_id(self, user_id, password):
        user = self.get_one_by_id(user_id)
        if user is not False and user.check_password(password) is True:
            return True
        return False

    def update_password_by_user_id(self, user_id, new_password):
        user = self.get_one_by_id(user_id)
        if user is not False:
            user.password = make_password(new_password)
            user.save()
            return True
        return False

    def delete_one_by_id(self, id):
        user = self.get_one_by_id(id)
        if user is not False:
            count, deleted = user.delete()
            return True if count > 0 else False
        return False

    def count_all(self):
        return User.objects.count()

    def get_all(self, offset=None, limit=None):
        if offset is None or limit is None:
            return User.objects.order_by("-date_joined").get()
        return User.objects.order_by("-date_joined")[offset : limit + offset]

    def truncate(self):
        return User.objects.all().delete()
