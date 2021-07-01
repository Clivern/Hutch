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

from django.views import View
from django.http import Http404
from django.shortcuts import render

from app.shortcuts import Logger
from app.shortcuts import get_config
from app.controllers.controller import Controller
from app.repository import GroupRepository
from app.module.group import Group as GroupModule


class ViewGroups(View, Controller):
    """ViewGroups Page Controller"""

    template_name = "templates/admin/group.list.html"

    def __init__(self):
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Group List Page
        """
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Weasel"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class CreateGroup(View, Controller):
    """CreateGroup Page Controller"""

    template_name = "templates/admin/group.create.html"

    def __init__(self):
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Create Group Page
        """
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Weasel"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class UpdateGroup(View, Controller):
    """UpdateGroup Page Controller"""

    template_name = "templates/admin/group.update.html"

    def __init__(self):
        self.group = GroupModule()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, group_id):
        """
        Update Group Page
        """
        group = self.group.get_one_by_id(group_id, request.user.id)

        if group is False:
            raise Http404("Group {} not found.".format(group_id))

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Weasel"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "group": group,
            },
        )
