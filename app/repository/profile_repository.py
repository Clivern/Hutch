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

from app.models import Profile


class ProfileRepository():
    """Profile Repository"""

    def profile_exists(self, user_id):
        try:
            user = Profile.objects.get(user=user_id)
            return False if user.pk is None else True
        except Exception:
            return False

    def create_profile(self, profile_data):
        if "user" not in profile_data:
            return False

        profile = Profile(
            job_title=profile_data["job_title"] if "job_title" in profile_data else "",
            company=profile_data["company"] if "company" in profile_data else "",
            personal_url=profile_data["personal_url"] if "personal_url" in profile_data else "",
            user=User.objects.get(pk=profile_data["user"])
        )

        profile.save()

        return False if profile.pk is None else profile

    def update_profile(self, profile_data):
        if "user" not in profile_data:
            return False

        profile = self.get_profile_by_user_id(profile_data["user"])

        if profile is not False:

            if "job_title" in profile_data:
                profile.job_title = profile_data["job_title"]

            if "company" in profile_data:
                profile.company = profile_data["company"]

            if "personal_url" in profile_data:
                profile.personal_url = profile_data["personal_url"]

            profile.save()
            return True
        else:
            self.create_profile(profile_data)
            return True

        return False

    def get_profile_by_user_id(self, user_id):
        try:
            profile = Profile.objects.get(user=user_id)
            return False if profile.pk is None else profile
        except Exception:
            return False

    def count_all_profiles(self):
        return Profile.objects.count()
