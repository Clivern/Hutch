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

from app.shortcuts import Logger
from app.repository import ClusterRepository


class Cluster:
    """Cluster Class"""

    def __init__(self):
        self.cluster = ClusterRepository()
        self.logger = Logger().get_logger(__name__)

    def get_one_by_id(self, id, user_id):
        """
        Get a Cluster by ID
        """
        return self.cluster.get_one_by_id(id, user_id)

    def create(self, data):
        """
        Create a Cluster
        """
        result = self.cluster.insert_one(data)

        if result:
            self.logger.info(
                "Create a cluster with id {} and name {}".format(result.id, result.name)
            )

        return result

    def update(self, id, data):
        """
        Update a Cluster By ID
        """
        self.logger.info("Update a cluster with id {}".format(id))

        return self.cluster.update_one_by_id(id, data)

    def delete_by_id(self, cluster_id, user_id):
        """
        Delete a Cluster By ID
        """
        self.logger.info("Delete a cluster with id {}".format(cluster_id))

        return self.cluster.delete_one_by_id(cluster_id, user_id)

    def get_user_clusters(self, user_id, offset, limit):
        """
        Get User Clusters
        """
        return self.cluster.get(user_id, offset, limit)

    def count_user_clusters(self, user_id):
        """
        Get User Clusters
        """
        return self.cluster.count_by_user(user_id)

    def count_hosts_by_cluster(self, cluster_id, user_id):
        """
        Count hosts by cluster id
        """
        return self.cluster.count_hosts_by_cluster(cluster_id, user_id)
