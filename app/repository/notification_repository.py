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

from app.models import Task
from app.models import Notification


class NotificationRepository:
    """Notification Repository"""

    def insert_one(self, data):
        """
        Insert Notification
        """
        notification = Notification(
            content=data["content"],
            kind=data["kind"],
            delivered=data["delivered"],
            user=User.objects.get(pk=data["user_id"]),
            task=Task.objects.get(pk=data["task_id"])
            if data["task_id"] is not None
            else None,
        )

        notification.save()
        return False if notification.pk is None else notification

    def insert_many(self, notifications):
        """
        Insert Many Notifications
        """
        status = True

        for notification in notifications:
            status &= True if self.insert_one(notification) is not False else False

        return status

    def get_one_by_id(self, id):
        """
        Get Notification By ID
        """
        try:
            notification = Notification.objects.get(pk=id)
            return False if notification.pk is None else notification
        except Exception:
            return False

    def get_one_by_task_id(self, task_id):
        """
        Get Notification By Task ID
        """
        try:
            notification = Notification.objects.get(task=task_id)
            return False if notification.pk is None else notification
        except Exception:
            return False

    def get_many_by_user(self, user_id, order_by, asc, count=5):
        """
        Get Many Notifications By User ID
        """
        notifications = Notification.objects.filter(user=user_id).order_by(
            order_by if asc else "-%s" % order_by
        )[:count]

        return notifications

    def update_one_by_id(self, id, data):
        """
        Update Notification By ID
        """
        notification = self.get_one_by_id(id)

        if notification is not False:
            if "content" in data:
                notification.content = data["content"]

            if "kind" in data:
                notification.kind = data["kind"]

            if "delivered" in data:
                notification.delivered = data["delivered"]

            if "user_id" in data:
                notification.user = User.objects.get(pk=data["user_id"])

            if "task_id" in data:
                notification.task = (
                    Task.objects.get(pk=data["task_id"])
                    if data["task_id"] is not None
                    else None
                )

            notification.save()
            return True
        return False

    def update_one_by_task_id(self, task_id, data):
        """
        Update Notification By Task ID
        """
        notification = self.get_one_by_task_id(task_id)

        if notification is not False:
            if "content" in data:
                notification.content = data["content"]

            if "kind" in data:
                notification.kind = data["kind"]

            if "delivered" in data:
                notification.delivered = data["delivered"]

            if "user_id" in data:
                notification.user = User.objects.get(pk=data["user_id"])

            if "task_id" in data:
                notification.task = (
                    Task.objects.get(pk=data["task_id"])
                    if data["task_id"] is not None
                    else None
                )

            notification.save()
            return True
        return False

    def get_one_by_id_and_user(self, id, user_id):
        """
        Delete Notification By ID and User ID
        """
        try:
            notification = Notification.objects.get(pk=id, user=user_id)
            return False if notification.pk is None else notification
        except Exception:
            return False

    def delete_one_by_id(self, id):
        """
        Delete Notification By ID
        """
        notification = self.get_one_by_id(id)

        if notification is not False:
            count, deleted = notification.delete()
            return True if count > 0 else False

        return False

    def count(self, user_id=None):
        """
        Count Notifications
        """
        if user_id is None:
            return Notification.objects.count()
        else:
            return Notification.objects.filter(user_id=user_id).count()

    def get(self, user_id, offset=None, limit=None):
        """
        Get Notifications By User ID
        """
        if offset is None or limit is None:
            return Notification.objects.filter(user_id=user_id).order_by("-created_at")

        return Notification.objects.filter(user_id=user_id).order_by("-created_at")[
            offset : limit + offset
        ]
