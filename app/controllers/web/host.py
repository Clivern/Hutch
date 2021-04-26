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
from app.repository import HostRepository


class ViewHost(View, Controller):
    """ViewHost Page Controller"""

    template_name = "templates/admin/host.index.html"

    def get(self, request, host_id):
        # Validate if host exists
        host_repository = HostRepository()
        host = host_repository.get_one_by_id(host_id)

        if host is False:
            raise Http404("Host {} not found.".format(host_id))

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Hutch"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "host": host,
            },
        )


class ViewHosts(View, Controller):
    """ViewHosts Page Controller"""

    template_name = "templates/admin/host.list.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Hutch"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class AddHost(View, Controller):
    """AddHost Page Controller"""

    template_name = "templates/admin/host.add.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Hutch"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
            },
        )


class EditHost(View, Controller):
    """EditHost Page Controller"""

    template_name = "templates/admin/host.edit.html"

    def get(self, request, host_id):
        # Validate if host exists
        host_repository = HostRepository()
        host = host_repository.get_one_by_id(host_id)

        if host is False:
            raise Http404("Host {} not found.".format(host_id))

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Hutch"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "host": host,
            },
        )
