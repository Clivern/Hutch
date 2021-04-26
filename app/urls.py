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
from app.controllers.web.host import AddHost
from app.controllers.web.host import EditHost
from app.controllers.web.host import ViewHosts

from app.controllers.web.group import AddGroup
from app.controllers.web.group import EditGroup
from app.controllers.web.group import ViewGroups

from app.controllers.web.key import AddKey
from app.controllers.web.key import ViewKeys

from app.controllers.web.user import AddUser
from app.controllers.web.user import EditUser
from app.controllers.web.user import ViewUsers

from app.controllers.web.settings import Settings
from app.controllers.web.profile import Profile
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

from app.controllers.api.v1.host import Host as HostEndpoint
from app.controllers.api.v1.host import Hosts as HostsEndpoint

from app.controllers.api.v1.key import Key as KeyEndpoint
from app.controllers.api.v1.key import Keys as KeysEndpoint
from app.controllers.api.v1.key import GenerateKey as GenerateKeyEndpoint

from app.controllers.api.v1.group import Group as GroupEndpoint
from app.controllers.api.v1.group import Groups as GroupsEndpoint

from app.controllers.api.v1.settings import Settings as SettingsEndpoint
from app.controllers.api.v1.profile import Profile as ProfileEndpoint
from app.controllers.api.v1.profile import Access as AccessEndpoint


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
                    "group/add",
                    AddGroup.as_view(),
                    name="app.web.admin.group.add",
                ),
                path(
                    "group/edit/<group_id>",
                    EditGroup.as_view(),
                    name="app.web.admin.group.edit",
                ),
                # Key Web Pages
                path("key", ViewKeys.as_view(), name="app.web.admin.key.list"),
                path(
                    "key/add",
                    AddKey.as_view(),
                    name="app.web.admin.key.add",
                ),
                # User Web Pages
                path("user", ViewUsers.as_view(), name="app.web.admin.user.list"),
                path(
                    "user/add",
                    AddUser.as_view(),
                    name="app.web.admin.user.add",
                ),
                path(
                    "user/edit/<user_id>",
                    EditUser.as_view(),
                    name="app.web.admin.user.edit",
                ),
                # Settings Page
                path("settings", Settings.as_view(), name="app.web.admin.settings"),
                # Profile Page
                path("profile", Profile.as_view(), name="app.web.admin.profile"),
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
                path(
                    "group",
                    GroupsEndpoint.as_view(),
                    name="app.api.v1.groups.endpoint",
                ),
                path(
                    "group/<group_id>",
                    GroupEndpoint.as_view(),
                    name="app.api.v1.group.endpoint",
                ),
                path(
                    "key",
                    KeysEndpoint.as_view(),
                    name="app.api.v1.keys.endpoint",
                ),
                path(
                    "action/key/generate",
                    GenerateKeyEndpoint.as_view(),
                    name="app.api.v1.key.generate.endpoint",
                ),
                path(
                    "key/<key_id>",
                    KeyEndpoint.as_view(),
                    name="app.api.v1.key.endpoint",
                ),
                # POST /api/v1/action/settings
                path(
                    "action/settings",
                    SettingsEndpoint.as_view(),
                    name="app.api.v1.settings.update.endpoint",
                ),
                # POST /api/v1/action/profile
                path(
                    "action/profile",
                    ProfileEndpoint.as_view(),
                    name="app.api.v1.profile.update.endpoint",
                ),
                # POST /api/v1/action/rotate_api_key
                path(
                    "action/rotate_api_key",
                    AccessEndpoint.as_view(),
                    name="app.api.v1.access.update.endpoint",
                ),
            ]
        ),
    ),
]

handler404 = handler404_view
handler500 = handler500_view
