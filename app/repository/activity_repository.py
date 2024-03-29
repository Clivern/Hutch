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

from app.models import Activity
from app.models import Organization


class ActivityRepository:
    """Activity Repository"""

    def insert_one(self, activity):
        """
        Insert a new activity
        """
        new_activity = Activity()

        if "activity" in activity:
            new_activity.activity = activity["activity"]

        if "user_id" in activity:
            new_activity.user = User.objects.get(pk=activity["user_id"])

        if "organization_id" in activity:
            new_activity.organization = Organization.objects.get(pk=activity["organization_id"])

        new_activity.save()

        return False if new_activity.pk is None else new_activity

    def update_one_by_id(self, id, activity_data):
        """
        Update activity by id
        """
        activity = self.get_one_by_id(id)

        if activity is not False:
            if "activity" in activity_data:
                activity.activity = activity_data["activity"]

            if "user_id" in activity_data:
                activity.user = User.objects.get(pk=activity_data["user_id"])

            if "organization_id" in activity_data:
                activity.organization = Organization.objects.get(pk=activity_data["organization_id"])

            activity.save()

            return True
        return False

    def count_all(self):
        """
        Count all activites
        """
        return Activity.objects.count()

    def count_by_user(self, user_id=None):
        """
        Count activites by user id
        """
        if user_id is None:
            return Activity.objects.count()
        else:
            return Activity.objects.filter(user_id=user_id).count()

    def count_by_organization(self, organization_id=None):
        """
        Count organization by organization id
        """
        if organization_id is None:
            return Organization.objects.count()
        else:
            return Organization.objects.filter(organization_id=organization_id).count()

    def get_all(self, offset=None, limit=None):
        """
        Get activities
        """
        if offset is None or limit is None:
            return Activity.objects.order_by("-created_at")

        return Activity.objects.order_by("-created_at")[offset : limit + offset]

    def get(self, user_id, offset=None, limit=None):
        """
        Get activities by user id
        """
        if offset is None or limit is None:
            return Activity.objects.filter(user_id=user_id).order_by("-created_at")

        return Activity.objects.filter(user_id=user_id).order_by("-created_at")[
            offset : limit + offset
        ]

    def get_one_by_id(self, id):
        """
        Delete activity by id
        """
        try:
            activity = Activity.objects.get(id=id)
            return False if activity.pk is None else activity
        except Exception:
            return False

    def delete_one_by_id(self, id):
        """
        Delete activity by id
        """
        activity = self.get_one_by_id(id)

        if activity is not False:
            count, deleted = activity.delete()
            return True if count > 0 else False

        return False
