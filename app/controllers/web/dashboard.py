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
from django.shortcuts import render

from app.shortcuts import Logger
from app.shortcuts import get_config
from app.controllers.controller import Controller
from app.module.profile import Profile as ProfileModule


class Dashboard(View, Controller):
    """Dashboard Page Controller"""

    template_name = "templates/dashboard.html"

    def __init__(self):
        self.profile = ProfileModule()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Dashboard Page
        """
        profile = self.profile.get_profile(request.user.id)

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Hutch"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "profile": profile,
            },
        )
