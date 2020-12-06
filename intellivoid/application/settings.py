from intellivoid import exceptions as service_exceptions
import requests
import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Settings(object):
    def __init__(self, application_id, secret_key, access_token,
                 endpoint="https://api.intellivoid.net/intellivoid/v1/application"):
        """
        Settings Public Constructor

        :param application_id:
        :param secret_key:
        :param access_token:
        :param endpoint:
        """
        self.endpoint = endpoint
        self.application_id = application_id
        self.secret_key = secret_key
        self.access_token = access_token

    def _send(self, path, **payload):
        """
        Sends a basic HTTP POST Request to the endpoint and handles any exceptions

        :param path:
        :param payload:
        :return:
        """

        payload["application_id"] = str(self.application_id)
        payload["secret_key"] = str(self.secret_key)
        payload["access_token"] = str(self.access_token)

        response = requests.post("{}/{}".format(self.endpoint, path), payload)
        request_id = None
        if "x-request-id" in response.headers:
            request_id = response.headers["x-request-id"]
        return service_exceptions.ServiceException.parse_and_raise(response.status_code,
                                                                   response.text,
                                                                   request_id)

    def get_summary(self, **parameters):
        """
        Returns a summary of all the settings/variables stored between the Application and the User.

        :param parameters:
        :return:
        """
        return self._send("settings/get_summary", **parameters)["results"]

    def add(self, variable_type, name, **parameters):
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

        return self._send("settings/add", **parameters)["results"]

    def dump(self, **parameters):
        """
        Dumps all the variables and they're values

        :param parameters:
        :return:
        """
        return self._send("settings/dump", **parameters)["results"]

    def clear(self, **parameters):
        """
        Deletes all existing variables

        :param parameters:
        :return:
        """
        return self._send("settings/clear", **parameters)["results"]

    def delete(self, name, **parameters):
        """
        Deletes a variable a key/index value in an list or array

        :param name:
        :param parameters:
        :return:
        """
        parameters["name"] = name
        return self._send("settings/delete", **parameters)["results"]

    def append(self, name, value, **parameters):
        """
        Appends a value to a list or array, for arrays you must include the key

        :param name:
        :param value:
        :param parameters:
        :return:
        """
        parameters["name"] = name
        parameters["value"] = value
        return self._send("settings/append", **parameters)["results"]

    def get(self, name, **parameters):
        """
        Gets the value of a variable

        :param name:
        :param parameters:
        :return:
        """
        parameters["name"] = name
        return self._send("settings/get", **parameters)["results"]