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

import json
from http import HTTPStatus

from django.views import View
from django.http import JsonResponse

from app.shortcuts import Logger
from app.controllers.controller import Controller
from app.repository.task_repository import TaskRepository
from app.exceptions.resource_not_found import ResourceNotFound


class GetTask(View, Controller):
    """GetTask Endpoint Controller"""

    def __init__(self):
        self.task_repository = TaskRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, task_id):
        """
        Fetch Task Data
        """
        self.logger.info("Fetch task with uuid {}".format(task_id))

        task = self.task_repository.get_one_by_uuid(task_id)

        if not task:
            self.logger.info("Task with uuid {} not found".format(task_id))
            raise ResourceNotFound("Task with uuid {} not found".format(task_id))

        self.logger.info("Found a task with uuid {}".format(task_id))

        return JsonResponse(
            {
                "id": task_id,
                "status": task.status.upper(),
                "result": json.loads(task.result),
                "createdAt": task.created_at,
                "updatedAt": task.updated_at,
            },
            status=HTTPStatus.OK,
        )
