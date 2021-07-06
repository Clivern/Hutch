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

import os
import shutil
from os.path import exists as file_exists

from app import APP_ROOT


class FileSystem:
    """FileSystem Class"""

    def read_file(self, file_path):
        """
        Read file content

        Args:
            file_path: The file path

        Returns:
            The file content
        """

        f = open(file_path, "r")

        return f.read()

    def create_dirs(self, path, mode=0o777):
        """
        Creates a dirs

        Args:
            path: The path
            mode: The mode

        Returns:
            Whether dirs got created or not
        """
        os.makedirs(path, mode)

        return os.path.exists(path)

    def file_exists(self, path):
        """
        Check if file exists

        Args:
            path: the file path

        Returns:
            Whether file exists or not
        """
        return file_exists(path)

    def list_sub_dirs(self, path):
        """
        Get a list of directories

        Args:
            path: the full path

        Returns:
            a list of sub directories
        """
        dirs = []

        for file in os.listdir(path):
            d = os.path.join(path, file)
            if os.path.isdir(d):
                dirs.append(d)

        return dirs

    def change_permission(self, path, mode=0o777):
        """
        Changes file permission

        Args:
            path: The path
            mode: The mode
        """
        os.chmod(path, mode)

    def open_file(self, file_path):
        """
        Open a file for read

        Args:
            file_path: The file path

        Returns:
            the opened file handler
        """

        return open(file_path, "r")

    def write_file(self, file_path, content):
        """
        Write content to a file

        Args:
            file_path: The file path
            content: The file content
        """

        f = open(file_path, "w")
        f.write(content)
        f.close()

    def delete_directory(self, directory):
        """
        Deletes a directory and its content

        Args:
            directory: The directory to delete
        """
        shutil.rmtree(directory)

    def delete_file(self, file_path):
        """
        Delete a file

        Args:
            file_path: The file path
        """
        os.remove(file_path)

    def storage_path(self, rel_file_path):
        """
        Get absolute path for a file or dir inside storage dir

        Args:
            rel_file_path: Relative file path from the root

        Returns:
            The storage path
        """
        return APP_ROOT + "/storage/" + rel_file_path.lstrip("/")

    def app_path(self, rel_file_path):
        """
        Get absolute path for a file or dir inside application dir

        Args:
            rel_file_path: Relative file path from the root

        Returns:
            The app path
        """
        return APP_ROOT + "/" + rel_file_path.lstrip("/")
