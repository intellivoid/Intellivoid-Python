#  Intellivoid - COA API Interface
#  Copyright (C) 2020 Intellivoid <https://github.com/intellivoid>
#
#  This file is part of the Intellivoid package.
#
#  This package is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This package is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this package.  If not, see <http://www.gnu.org/licenses/>.

from intellivoid import exceptions as service_exceptions
import httpx
import json
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Settings(object):
    """
    Settings public object

    :param application_id:
    :param secret_key:
    :param access_token:
    :param endpoint:
    """

    def __init__(self, application_id, secret_key, access_token,
                 endpoint="https://api.intellivoid.net/intellivoid/v1/application"):
        """
        Settings Public Constructor
        """

        self.endpoint = endpoint
        self.application_id = application_id
        self.secret_key = secret_key
        self.access_token = access_token

    async def _send(self, path, **payload):
        """
        Sends a basic HTTP POST Request to the endpoint and handles any exceptions

        :param path:
        :param payload:
        :return:
        """

        payload["application_id"] = str(self.application_id)
        payload["secret_key"] = str(self.secret_key)
        payload["access_token"] = str(self.access_token)
        async with httpx.AsyncClient() as client:
            response = await client.post("{}/{}".format(self.endpoint, path), data=payload)
            request_id = None
            if "x-request-id" in response.headers:
                request_id = response.headers["x-request-id"]
        return service_exceptions.ServiceException.parse_and_raise(response.status_code,
                                                                   response.text,
                                                                   request_id)

    async def get_summary(self, **parameters):
        """
        Returns a summary of all the settings/variables stored between the Application and the User.

        :param parameters:
        :return:
        """

        return (await self._send("settings/get_summary", **parameters))["results"]

    async def add(self, variable_type, name, **parameters):
        """
        Adds or updates a new variable to the Application's settings

        :param variable_type:
        :param name:
        :param parameters:
        :return:
        """

        parameters["type"] = variable_type
        parameters["name"] = name
        if "value" in parameters:
            if type(parameters["value"]) is list:
                # Serialize the value to json if it's a list so it's understood by the server
                parameters["value"] = json.dumps(parameters["value"])
            if type(parameters["value"]) is dict:
                # Serialize the value to json if it's a dict so it's understood by the server
                parameters["value"] = json.dumps(parameters["value"])
        return (await self._send("settings/add", **parameters))["results"]

    async def dump(self, **parameters):
        """
        Dumps all the variables and they're values

        :param parameters:
        :return:
        """

        return (await self._send("settings/dump", **parameters))["results"]

    async def clear(self, **parameters):
        """
        Deletes all existing variables

        :param parameters:
        :return:
        """

        return (await self._send("settings/clear", **parameters))["results"]

    async def delete(self, name, **parameters):
        """
        Deletes a variable a key/index value in an list or array

        :param name:
        :param parameters:
        :return:
        """

        parameters["name"] = name
        return (await self._send("settings/delete", **parameters))["results"]

    async def append(self, name, value, **parameters):
        """
        Appends a value to a list or array, for arrays you must include the key

        :param name:
        :param value:
        :param parameters:
        :return:
        """

        parameters["name"] = name
        parameters["value"] = value
        return (await self._send("settings/append", **parameters))["results"]

    async def get(self, name, **parameters):
        """
        Gets the value of a variable

        :param name:
        :param parameters:
        :return:
        """

        parameters["name"] = name
        return (await self._send("settings/get", **parameters))["results"]
