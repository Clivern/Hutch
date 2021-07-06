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

from app.models import Option


class OptionRepository:
    """Option Repository"""

    def insert_one(self, option):
        """
        Insert a New Option
        """
        option = Option(
            name=option["name"],
            value=option["value"],
            autoload=option["autoload"] if "autoload" in option else False,
        )

        option.save()
        return False if option.pk is None else option

    def insert_many(self, options):
        """
        Insert Many Options
        """
        status = True

        for option in options:
            status &= True if self.insert_one(option) is not False else False

        return status

    def get_one_by_id(self, id):
        """
        Get Option By ID
        """
        try:
            option = Option.objects.get(pk=id)
            return False if option.pk is None else option
        except Exception:
            return False

    def get_one_by_name(self, name):
        """
        Get Option By Name
        """
        try:
            option = Option.objects.get(name=name)
            return False if option.pk is None else option
        except Exception:
            return False

    def get_value_by_name(self, name, default=""):
        """
        Get Option Value By Name
        """
        try:
            option = Option.objects.get(name=name)
            return default if option.pk is None else option.value
        except Exception:
            return default

    def get_many_by_autoload(self, autoload):
        """
        Get Many Options By Autoload
        """
        options = Option.objects.filter(autoload=autoload)
        return options

    def get_many_by_names(self, names):
        """
        Get Many Options By Names
        """
        options = Option.objects.filter(name__in=names)
        return options

    def update_value_by_id(self, id, value):
        """
        Update Option Value By ID
        """
        option = self.get_one_by_id(id)

        if option is not False:
            option.value = value
            option.save()

            return True

        return False

    def update_value_by_name(self, name, value):
        """
        Update Option Value By Name
        """
        option = self.get_one_by_name(name)

        if option is not False:
            option.value = value
            option.save()

            return True

        return False

    def count(self):
        """
        Count all options
        """
        return Option.objects.count()

    def delete_one_by_id(self, id):
        """
        Delete Option By ID
        """
        option = self.get_one_by_id(id)

        if option is not False:
            count, deleted = option.delete()
            return True if count > 0 else False

        return False

    def delete_one_by_name(self, name):
        """
        Delete Option By Name
        """
        option = self.get_one_by_name(name)

        if option is not False:
            count, deleted = option.delete()
            return True if count > 0 else False

        return False

    def truncate(self):
        """
        Truncate all options
        """
        return Option.objects.all().delete()
