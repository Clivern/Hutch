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

from app.models import Host
from app.models import HostMeta


class HostRepository:
    """Host Repository"""

    def insert_one(self, host_data):
        """
        Insert a new host
        """
        host = Host()

        if "name" in host_data:
            host.name = host_data["name"]

        if "uuid" in host_data:
            host.uuid = host_data["uuid"]

        if "hostname" in host_data:
            host.hostname = host_data["hostname"]

        if "ipaddress" in host_data:
            host.ipaddress = host_data["ipaddress"]

        host.save()

        return False if host.pk is None else host

    def update_one_by_id(self, host_uuid, host_data):
        """
        Updates a host by UUID
        """
        host = self.get_one_by_id(host_uuid)

        if host is not False:
            if "name" in host_data:
                host.name = host_data["name"]

            if "uuid" in host_data:
                host.uuid = host_data["uuid"]

            if "hostname" in host_data:
                host.hostname = host_data["hostname"]

            if "ipaddress" in host_data:
                host.ipaddress = host_data["ipaddress"]

            host.save()
            return True

        return False

    def get_one_by_id(self, host_uuid):
        """
        Get host by a UUID
        """
        try:
            host = Host.objects.get(uuid=host_uuid)
            return False if host.pk is None else host
        except Exception:
            return False

    def delete_one_by_id(self, host_uuid):
        """
        Delete host by a UUID
        """
        host = self.get_one_by_id(host_uuid)

        if host is not False:
            count, deleted = host.delete()
            return True if count > 0 else False

        return False
