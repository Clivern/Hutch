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

from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login

from app.exceptions.access_forbidden import AccessForbidden
from app.repository.option_repository import OptionRepository


def login_if_not_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if not request.user or not request.user.is_authenticated:
            return redirect(
                reverse("app.web.login") + "?redirect=" + request.get_full_path()
            )
        return function(controller, request, *args, **kwargs)

    return wrap


def redirect_if_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return redirect(reverse("app.web.admin.dashboard"))
        return function(controller, request, *args, **kwargs)

    return wrap


def stop_request_if_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            raise AccessForbidden(_("Error! Access forbidden for authenticated users."))
        return function(controller, request, *args, **kwargs)

    return wrap


def prevent_if_not_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        # API authentication
        api_key = request.headers.get("x-api-key")
        user = authenticate(request, api_key=api_key)

        if user is not None:
            login(request, user)
            return function(controller, request, *args, **kwargs)

        # UI Authentication
        if not request.user or not request.user.is_authenticated:
            raise AccessForbidden(_("Oops! Access forbidden."))

        return function(controller, request, *args, **kwargs)

    return wrap


def allow_if_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if not request.user or not request.user.is_authenticated:
            return JsonResponse({"errorMessage": _("Oops! Access forbidden.")})
        return function(controller, request, *args, **kwargs)

    return wrap


def redirect_if_not_installed(function):
    def wrap(controller, request, *args, **kwargs):
        installed = (
            False
            if OptionRepository().get_one_by_name("app_installed") is False
            else True
        )
        if not installed:
            return redirect("app.web.install")
        return function(controller, request, *args, **kwargs)

    return wrap


def stop_request_if_installed(function):
    def wrap(controller, request, *args, **kwargs):
        installed = (
            False
            if OptionRepository().get_one_by_name("app_installed") is False
            else True
        )
        if installed:
            return JsonResponse(
                {"errorMessage": _("Error! Application is already installed.")}
            )
        return function(controller, request, *args, **kwargs)

    return wrap
