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

from app.models import Server
from app.models import ServerMeta


class ServerRepository():
    """Server Repository"""

    def insert_one(self, server_data):
        """
        Insert a new server

        Args:
            server_data: The server data

        Returns:
            The server object or False
        """
        server = Server()

        if "name" in server_data:
            server.name = server_data["name"]

        if "uuid" in server_data:
            server.uuid = server_data["uuid"]

        if "hostname" in server_data:
            server.hostname = server_data["hostname"]

        if "ipaddress" in server_data:
            server.ipaddress = server_data["ipaddress"]

        server.save()

        return False if server.pk is None else server

    def update_one_by_id(self, server_uuid, server_data):
        """
        Updates a server by UUID

        Args:
            server_uuid: The server UUID
            server_data: The server data

        Returns:
            Whether object updated or not
        """
        server = self.get_one_by_id(server_uuid)

        if server is not False:
            if "name" in server_data:
                server.name = server_data["name"]

            if "uuid" in server_data:
                server.uuid = server_data["uuid"]

            if "hostname" in server_data:
                server.hostname = server_data["hostname"]

            if "ipaddress" in server_data:
                server.ipaddress = server_data["ipaddress"]

            server.save()
            return True

        return False

    def get_one_by_id(self, server_uuid):
        """
        Get server by a UUID

        Args:
            server_uuid: The server UUID

        Returns:
            The server or False
        """
        try:
            server = Server.objects.get(uuid=server_uuid)
            return False if server.pk is None else server
        except Exception:
            return False

    def add_tag(self, server_uuid, tag_key, tag_value):
        """
        Add a server tag

        Args:
            server_uuid: The server UUID
            tag_key: The tag key
            tag_value: The tag value

        Returns:
            Whether tag added or not
        """
        pass

    def update_tag(self, server_uuid, tag_key, tag_value):
        """
        Updates a server tag

        Args:
            server_uuid: The server UUID
            tag_key: The tag key
            tag_value: The tag value

        Returns:
            Whether tag updated or not
        """
        pass

    def get_tags(self, server_uuid):
        """
        Get server tags with UUID

        Args:
            server_uuid: The server UUID

        Returns:
            The server tags
        """
        pass

    def remove_tag(self, meta_id):
        """
        Remove a server tag

        Args:
            meta_id: The meta ID

        Returns:
            Whether tag deleted or not
        """
        meta = ServerMeta.objects.get(id=meta_id)

        if meta is not False:
            count, deleted = meta.delete()
            return True if count > 0 else False

        return False

    def delete_one_by_id(self, server_uuid):
        """
        Delete server by a UUID

        Args:
            server_uuid: The server UUID

        Returns:
            Whether object got deleted or not
        """
        server = self.get_one_by_id(server_uuid)

        if server is not False:
            count, deleted = server.delete()
            return True if count > 0 else False

        return False
