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
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils.translation import gettext as _

from app.controllers.controller import Controller
from app.helpers.decorators import login_if_not_authenticated


class Logout(View, Controller):
    """Logout Controller"""

    @login_if_not_authenticated
    def get(self, request):
        """
        Logout Page
        """
        logout(request)
        messages.success(request, _("You've been logged out successfully"))
        return redirect("app.web.login")
