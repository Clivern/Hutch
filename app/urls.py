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


urlpatterns = [
    path('', Home.as_view(), name='app.web.home'),
    path('_health', Health.as_view(), name='app.web.health'),
    path('_ready', Ready.as_view(), name='app.web.ready'),
    path('login', Login.as_view(), name='app.web.login'),
    path('install', Install.as_view(), name='app.web.install'),
    path('forgot-password', ForgotPassword.as_view(), name='app.web.forgot_password'),
    path('reset-password/<token>', ResetPassword.as_view(), name='app.web.reset_password'),

    path('admin/', include([
        path('logout', Logout.as_view(), name='app.web.admin.logout'),
        path('dashboard', Dashboard.as_view(), name='app.web.admin.dashboard'),
    ])),

    # Public v1 API
    path('api/v1/', include([
        # GET /api/v1/task/<id>
        path('task/<id>', GetTask.as_view(), name='app.api.v1.task.get_task.endpoint'),
        # POST /api/v1/login
        path('login', LoginEndpoint.as_view(), name='app.api.v1.auth.login.endpoint'),
        # POST /api/v1/forgot-password
        path('forgot-password', ForgotPasswordEndpoint.as_view(), name='app.api.v1.auth.forgot_password.endpoint'),
        # POST /api/v1/reset-password
        path('reset-password', ResetPasswordEndpoint.as_view(), name='app.api.v1.auth.reset_password.endpoint'),
        # POST /api/v1/install
        path('install', InstallEndpoint.as_view(), name='app.api.v1.install.install.endpoint'),
    ])),
]

handler404 = handler404_view
handler500 = handler500_view
