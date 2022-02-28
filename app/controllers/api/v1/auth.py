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

from http import HTTPStatus

from django.views import View
from django.http import JsonResponse

from app.shortcuts import Logger
from app.controllers.controller import Controller


class Login(View, Controller):
    """Login Endpoint Controller"""

    def __init__(self):
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        return JsonResponse({}, status=HTTPStatus.OK)


class ForgotPassword(View, Controller):
    """ForgotPassword Endpoint Controller"""

    def __init__(self):
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        return JsonResponse({}, status=HTTPStatus.OK)


class ResetPassword(View, Controller):
    """ResetPassword Endpoint Controller"""

    def __init__(self):
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        return JsonResponse({}, status=HTTPStatus.OK)
