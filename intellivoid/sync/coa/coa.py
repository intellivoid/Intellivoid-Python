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
#  along with this package. If not, see <http://www.gnu.org/licenses/>.

from intellivoid import exceptions as service_exceptions
from intellivoid.sync.coa import exceptions as coa_exceptions
import requests

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class CrossOverAuthentication(object):
    def __init__(self,
                 endpoint="https://api.intellivoid.net/intellivoid/v1/coa",
                 accounts_endpoint="https://accounts.intellivoid.net"):
        """
        CrossOverAuthentication Public Constructor

        :param endpoint:
        :param accounts_endpoint:
        """
        self.accounts_endpoint = accounts_endpoint
        self.endpoint = endpoint

    def _send(self, path, **payload):
        """
        Sends a basic HTTP POST Request to the endpoint and handles any exceptions
        related to COA

        :param path:
        :param payload:
        :return:
        """
        response = requests.post("{}/{}".format(self.endpoint, path), payload)
        request_id = None
        if "x-request-id" in response.headers:
            request_id = response.headers["x-request-id"]
        return service_exceptions.ServiceException.parse_and_raise(response.status_code,
                                                                   response.text,
                                                                   request_id)

    def request_authentication(self, application_id, **parameters):
        """
        Request Authentication to the user by requesting an Authentication Request Token and
        redirecting the user to the authentication link returned on the response

        :param application_id:
        :param parameters:
        :return:
        """
        parameters["application_id"] = application_id
        return self._send("auth/request_authentication", **parameters)["results"]

    def process_authentication(self, application_id, secret_key, request_token, poll_results=True, **parameters):
        """
        Processes the authentication request, if the user authenticates then the method will return the results

        :param application_id:
        :param secret_key:
        :param request_token:
        :param poll_results:
        :param parameters:
        :return:
        """
        parameters["application_id"] = application_id
        parameters["secret_key"] = secret_key,
        parameters["request_token"] = request_token

        if poll_results:
            while True:
                try:
                    return self._send("auth/process_authentication", **parameters)["results"]
                except coa_exceptions.AwaitingAuthentication:
                    # We're waiting for the user to authenticate, so this isn't an error that we should raise
                    pass
        return self._send("auth/process_authentication", **parameters)["results"]

    def get_application(self, application_id, **parameters):
        """
        Gets Public Information about the Application using the Application ID

        :param application_id:
        :param parameters:
        :return:
        """
        parameters["application_id"] = application_id
        return self._send("../application", **parameters)["results"]

    def get_access_token(self, application_id, secret_key, access_token, **parameters):
        """
        Returns the details about the Access Token, the same as process_authentication() but without the
        access_token being returned in the response

        :param application_id:
        :param secret_key:
        :param access_token:
        :param parameters:
        :return:
        """
        parameters["application_id"] = application_id
        parameters["secret_key"] = secret_key,
        parameters["access_token"] = access_token

        return self._send("auth/get_access_token", **parameters)["results"]

    def create_authentication_url(self, application_id, redirect, **parameters):
        """
        Creates a standard authentication URL which will automatically generate
        a request token upon visiting and redirect the user to the redirect URL
        with the access token in the GET parameter

        :param application_id:
        :param redirect:
        :param parameters:
        :return:
        """
        parameters["action"] = "request_authentication"
        parameters["application_id"] = application_id
        parameters["redirect"] = redirect

        return "{}/auth/coa?{}".format(self.accounts_endpoint, urlencode(parameters))
