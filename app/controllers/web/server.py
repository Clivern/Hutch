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
from app.repository.server_repository import ServerRepository


class ViewServer(View, Controller):
    """ViewServer Page Controller"""

    template_name = 'templates/admin/server.view_one.html'

    def get(self, request, server_id):
        # Validate if server exists
        server_repository = ServerRepository()
        server = server_repository.get_server_by_id(server_id)

        if server is False:
            raise Http404("Server {} not found.".format(server_id))

        return render(request, self.template_name, {
            "title": get_config("app_name", "Hustle"),
            "description": get_config("app_description", ""),
            "base_url": get_config("app_url", ""),
            "server": server,
        })


class ViewServers(View, Controller):
    """ViewServers Page Controller"""

    template_name = 'templates/admin/server.view_many.html'

    def get(self, request):
        return render(request, self.template_name, {
            "title": get_config("app_name", "Hustle"),
            "description": get_config("app_description", ""),
            "base_url": get_config("app_url", ""),
        })


class CreateServer(View, Controller):
    """CreateServer Page Controller"""

    template_name = 'templates/admin/server.create.html'

    def get(self, request):
        return render(request, self.template_name, {
            "title": get_config("app_name", "Hustle"),
            "description": get_config("app_description", ""),
            "base_url": get_config("app_url", ""),
        })


class UpdateServer(View, Controller):
    """UpdateServer Page Controller"""

    template_name = 'templates/admin/server.update.html'

    def get(self, request, server_id):
        # Validate if server exists
        server_repository = ServerRepository()
        server = server_repository.get_server_by_id(server_id)

        if server is False:
            raise Http404("Server {} not found.".format(server_id))

        return render(request, self.template_name, {
            "title": get_config("app_name", "Hustle"),
            "description": get_config("app_description", ""),
            "base_url": get_config("app_url", ""),
            "server": server,
        })
