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
from app.repository import KeyRepository


class ViewKey(View, Controller):
    """ViewKey Page Controller"""

    template_name = "templates/admin/key.view_one.html"

    def get(self, request, key_id):
        # Validate if key exists
        key_repository = KeyRepository()
        key = key_repository.get_one_by_id(key_id)

        if key is False:
            raise Http404("Key {} not found.".format(key_id))

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Chestnut"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "key": key,
            },
        )


class ViewKeys(View, Controller):
    """ViewKeys Page Controller"""

    template_name = "templates/admin/key.view_many.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Chestnut"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class CreateKey(View, Controller):
    """CreateKey Page Controller"""

    template_name = "templates/admin/key.create.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Chestnut"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class UpdateKey(View, Controller):
    """UpdateKey Page Controller"""

    template_name = "templates/admin/key.update.html"

    def get(self, request, key_id):
        # Validate if key exists
        key_repository = KeyRepository()
        key = key_repository.get_one_by_id(key_id)

        if key is False:
            raise Http404("Key {} not found.".format(key_id))

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Chestnut"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "key": key,
            },
        )
