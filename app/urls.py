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

from django.urls import include, path

from app.controllers.web.home import Home
from app.controllers.web.ready import Ready
from app.controllers.web.health import Health
from app.controllers.web.login import Login
from app.controllers.web.logout import Logout
from app.controllers.web.install import Install

from app.controllers.web.host import ViewHost
from app.controllers.web.host import CreateHost
from app.controllers.web.host import UpdateHost
from app.controllers.web.host import ViewHosts

from app.controllers.web.group import ViewGroup
from app.controllers.web.group import CreateGroup
from app.controllers.web.group import UpdateGroup
from app.controllers.web.group import ViewGroups

from app.controllers.web.key import ViewKey
from app.controllers.web.key import CreateKey
from app.controllers.web.key import UpdateKey
from app.controllers.web.key import ViewKeys

from app.controllers.web.user import ViewUser
from app.controllers.web.user import CreateUser
from app.controllers.web.user import UpdateUser
from app.controllers.web.user import ViewUsers

from app.controllers.web.settings import Settings
from app.controllers.web.dashboard import Dashboard
from app.controllers.web.forgot_password import ForgotPassword
from app.controllers.web.reset_password import ResetPassword
from app.controllers.web.error import handler404 as handler404_view
from app.controllers.web.error import handler500 as handler500_view

from app.controllers.api.v1.task import GetTask
from app.controllers.api.v1.auth import Login as LoginEndpoint
from app.controllers.api.v1.install import Install as InstallEndpoint
from app.controllers.api.v1.auth import ResetPassword as ResetPasswordEndpoint
from app.controllers.api.v1.auth import ForgotPassword as ForgotPasswordEndpoint

from app.controllers.api.v1.host import GetHost as GetHostEndpoint
from app.controllers.api.v1.host import GetHosts as GetHostsEndpoint
from app.controllers.api.v1.host import CreateHost as CreateHostEndpoint
from app.controllers.api.v1.host import UpdateHost as UpdateHostEndpoint
from app.controllers.api.v1.host import DeleteHost as DeleteHostEndpoint
from app.controllers.api.v1.settings import Settings as SettingsEndpoint


urlpatterns = [
    path("", Home.as_view(), name="app.web.home"),
    path("_health", Health.as_view(), name="app.web.health"),
    path("_ready", Ready.as_view(), name="app.web.ready"),
    path("login", Login.as_view(), name="app.web.login"),
    path("install", Install.as_view(), name="app.web.install"),
    path("forgot-password", ForgotPassword.as_view(), name="app.web.forgot_password"),
    path(
        "reset-password/<token>", ResetPassword.as_view(), name="app.web.reset_password"
    ),
    path(
        "admin/",
        include(
            [
                path("logout", Logout.as_view(), name="app.web.admin.logout"),
                path("dashboard", Dashboard.as_view(), name="app.web.admin.dashboard"),
                # Group Web Pages
                path("group", ViewGroups.as_view(), name="app.web.admin.group.list"),
                path(
                    "group/<group_id>",
                    ViewGroup.as_view(),
                    name="app.web.admin.group.view",
                ),
                path(
                    "group/create",
                    CreateGroup.as_view(),
                    name="app.web.admin.group.add",
                ),
                path(
                    "group/update/<group_id>",
                    UpdateGroup.as_view(),
                    name="app.web.admin.group.edit",
                ),
                # Key Web Pages
                path("key", ViewKeys.as_view(), name="app.web.admin.key.list"),
                path(
                    "key/<key_id>",
                    ViewKey.as_view(),
                    name="app.web.admin.key.view",
                ),
                path(
                    "key/create",
                    CreateKey.as_view(),
                    name="app.web.admin.key.add",
                ),
                path(
                    "key/update/<key_id>",
                    UpdateKey.as_view(),
                    name="app.web.admin.key.edit",
                ),
                # Host Web Pages
                path("host", ViewHosts.as_view(), name="app.web.admin.host.list"),
                path(
                    "host/<host_id>",
                    ViewHost.as_view(),
                    name="app.web.admin.host.view",
                ),
                path(
                    "host/create",
                    CreateHost.as_view(),
                    name="app.web.admin.host.add",
                ),
                path(
                    "host/update/<host_id>",
                    UpdateHost.as_view(),
                    name="app.web.admin.host.edit",
                ),
                # User Web Pages
                path("user", ViewUsers.as_view(), name="app.web.admin.user.list"),
                path(
                    "user/<user_id>",
                    ViewUser.as_view(),
                    name="app.web.admin.user.view",
                ),
                path(
                    "user/create",
                    CreateUser.as_view(),
                    name="app.web.admin.user.add",
                ),
                path(
                    "user/update/<user_id>",
                    UpdateUser.as_view(),
                    name="app.web.admin.user.edit",
                ),
                # Settings Page
                path("settings", Settings.as_view(), name="app.web.admin.settings"),
            ]
        ),
    ),
    # Public v1 API
    path(
        "api/v1/",
        include(
            [
                # GET /api/v1/task/<id>
                path(
                    "task/<task_id>",
                    GetTask.as_view(),
                    name="app.api.v1.task.get_task.endpoint",
                ),
                # POST /api/v1/login
                path(
                    "login",
                    LoginEndpoint.as_view(),
                    name="app.api.v1.auth.login.endpoint",
                ),
                # POST /api/v1/forgot-password
                path(
                    "forgot-password",
                    ForgotPasswordEndpoint.as_view(),
                    name="app.api.v1.auth.forgot_password.endpoint",
                ),
                # POST /api/v1/reset-password
                path(
                    "reset-password",
                    ResetPasswordEndpoint.as_view(),
                    name="app.api.v1.auth.reset_password.endpoint",
                ),
                # POST /api/v1/install
                path(
                    "install",
                    InstallEndpoint.as_view(),
                    name="app.api.v1.install.install.endpoint",
                ),
                # GET /api/v1/host
                path(
                    "host",
                    GetHostsEndpoint.as_view(),
                    name="app.api.v1.host.get_many.endpoint",
                ),
                # POST /api/v1/host
                path(
                    "host",
                    CreateHostEndpoint.as_view(),
                    name="app.api.v1.host.create.endpoint",
                ),
                # GET /api/v1/host/<host_id>
                path(
                    "host/<host_id>",
                    GetHostEndpoint.as_view(),
                    name="app.api.v1.host.get_one.endpoint",
                ),
                # PUT /api/v1/host/<host_id>
                path(
                    "host/<host_id>",
                    UpdateHostEndpoint.as_view(),
                    name="app.api.v1.host.update.endpoint",
                ),
                # POST /api/v1/action/settings
                path(
                    "action/settings",
                    SettingsEndpoint.as_view(),
                    name="app.api.v1.settings.update.endpoint",
                ),
            ]
        ),
    ),
]

handler404 = handler404_view
handler500 = handler500_view
