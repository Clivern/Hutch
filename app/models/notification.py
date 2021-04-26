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

from django.db import models
from django.contrib.auth.models import User

from .task import Task
from .organization import Organization


class Notification(models.Model):
    """Notification Model"""

    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

    KIND_CHOICES = (
        ("running", "RUNNING"),
        ("success", "SUCCESS"),
        ("failed", "FAILED"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name="Related user"
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Parent Organization",
        null=False,
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related Task",
        null=True,
    )

    content = models.CharField(max_length=200, verbose_name="Content")
    kind = models.CharField(
        max_length=20, choices=KIND_CHOICES, default="message", verbose_name="Kind"
    )
    delivered = models.BooleanField(default=False, verbose_name="Delivered")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "app_notification"
