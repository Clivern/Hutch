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


class Organization(models.Model):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"

    STATUS_CHOICES = (("ACTIVE", ACTIVE), ("DISABLED", DISABLED))

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Owner User",
        null=False,
    )

    uuid = models.CharField(max_length=60, verbose_name="UUID")
    name = models.CharField(max_length=60, verbose_name="Name")
    slug = models.CharField(max_length=60, verbose_name="Slug")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="ACTIVE", verbose_name="Status"
    )
    disabled_at = models.DateTimeField(verbose_name="Disabled at", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "app_organization"
