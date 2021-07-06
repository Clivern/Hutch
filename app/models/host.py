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
from .group import Group
from .key import Key


class Host(models.Model):
    """Host Model"""

    PENDING = "pending"
    RUNNING = "running"
    STOPPED = "stopped"
    MISSING = "missing"

    STATUS_CHOICES = (
        ("pending", PENDING),
        ("running", RUNNING),
        ("stopped", STOPPED),
        ("missing", MISSING),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name="Related user"
    )

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, db_index=True, verbose_name="Related Group"
    )

    key = models.ForeignKey(
        Key, on_delete=models.CASCADE, db_index=True, verbose_name="Related Key"
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Status"
    )

    name = models.CharField(max_length=100, verbose_name="Name")
    uuid = models.CharField(max_length=60, db_index=True, verbose_name="uuid")
    cloud_provider = models.CharField(max_length=50, verbose_name="Cloud Provider")
    specification = models.TextField(verbose_name="Specifications")
    hostname = models.CharField(max_length=100, verbose_name="Hostname")
    remote_id = models.CharField(max_length=100, verbose_name="Remote ID")
    username = models.CharField(max_length=100, verbose_name="Username")
    ipaddress = models.CharField(max_length=100, verbose_name="IP Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.uuid

    class Meta:
        db_table = "app_host"
