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

from app.shortcuts import get_config
from app.controllers.controller import Controller
from app.repository import UserRepository


class ViewUsers(View, Controller):
    """ViewUsers Page Controller"""

    template_name = "templates/admin/user.list.html"

    def __init__(self):
        self.user = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Weasel"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class AddUser(View, Controller):
    """AddUser Page Controller"""

    template_name = "templates/admin/user.add.html"

    def __init__(self):
        self.user = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Weasel"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class EditUser(View, Controller):
    """EditUser Page Controller"""

    template_name = "templates/admin/user.edit.html"

    def __init__(self):
        self.user = UserRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, user_id):
        # Validate if user exists
        user = self.user.get_one_by_id(user_id)

        if user is False:
            raise Http404("User {} not found.".format(user_id))

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Weasel"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "user": user,
            },
        )
