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

import requests
import json

from app.shortcuts import Logger
from app.exceptions import ApiError


class Digitalocean:
    """Digitalocean Class"""

    API_URL = "https://api.digitalocean.com/v2"

    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.digitalocean.com/v2"
        self.logger = Logger().get_logger(__name__)

    def _get_headers(self):
        """
        Get Headers
        """
        return {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json",
        }

    def create_ssh_key(self, name, public_key):
        """
        Create SSH Key
        """
        payload = {"name": name, "public_key": public_key}

        response = requests.post(
            "{}/account/keys".format(Digitalocean.API_URL),
            headers=self._get_headers(),
            json=payload,
        )

        if response.status_code // 100 != 2:
            raise ApiError(
                "Digitalocean respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))

    def list_ssh_keys(self):
        """
        List SSH Keys
        """
        response = requests.get(
            "{}/account/keys".format(Digitalocean.API_URL), headers=self._get_headers()
        )

        if response.status_code // 100 != 2:
            raise ApiError(
                "Digitalocean respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))["ssh_keys"]

    def create_droplet(self, name, region, size, image, ssh_keys=[]):
        """
        Create a Droplet
        """
        data = {
            "name": name,
            "region": region,
            "size": size,
            "image": image,
            "ssh_keys": ssh_keys,
            "backups": False,
            "ipv6": True,
            "user_data": None,
            "volumes": None,
            "with_droplet_agent": True,
            "tags": ["weasel"],
        }

        response = requests.post(
            "{}/droplets".format(Digitalocean.API_URL),
            headers=self._get_headers(),
            json=data,
        )

        if response.status_code // 100 != 2:
            raise ApiError(
                "Digitalocean respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))["droplet"]

    def get_droplet(self, droplet_id):
        """
        Get Droplet
        """
        response = requests.get(
            "{}/droplets/{}".format(Digitalocean.API_URL, droplet_id),
            headers=self._get_headers(),
        )

        if response.status_code // 100 != 2:
            raise ApiError(
                "Digitalocean respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))["droplet"]

    def power_on_droplet(self, droplet_id):
        """
        Start Droplet
        """
        data = {"type": "power_on"}

        response = requests.post(
            "{}/droplets/{}/actions".format(Digitalocean.API_URL, droplet_id),
            headers=self._get_headers(),
            json=data,
        )

        if response.status_code // 100 != 2:
            raise ApiError(
                "Digitalocean respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))

    def destroy_droplet(self, droplet_id):
        """
        Destroy a Droplet
        """
        response = requests.delete(
            "{}/droplets/{}".format(Digitalocean.API_URL, droplet_id),
            headers=self._get_headers(),
        )

        if response.status_code // 100 != 2:
            raise ApiError(
                "Digitalocean respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return True
