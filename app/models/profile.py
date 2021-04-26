# Copyright 2022 Clivern
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

from django.db import models
from django.contrib.auth.models import User

from .organization import Organization


class Profile(models.Model):
    """Profile Model"""

    LIGHT = "light"
    DARK = "dark"

    THEME_CHOICES = (("light", LIGHT), ("dark", DARK))

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related user",
        null=False,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Parent Organization",
        null=False,
    )

    theme = models.CharField(
        max_length=20, choices=THEME_CHOICES, default="light", verbose_name="Theme"
    )
    company = models.CharField(default="", max_length=60, verbose_name="Company")
    team = models.CharField(default="", max_length=60, verbose_name="Team")
    job_title = models.CharField(default="", max_length=100, verbose_name="Job Title")
    personal_url = models.CharField(
        default="", max_length=100, verbose_name="Personal URL"
    )
    api_key = models.CharField(default="", max_length=100, verbose_name="API Key")
    timezone = models.CharField(default="", max_length=50, verbose_name="Timezone")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "app_profile"
