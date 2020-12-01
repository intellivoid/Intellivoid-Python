from . import exception

import requests

__all__ = ["CrossOverAuthentication"]


class CrossOverAuthentication(object):
    def __init__(self, endpoint="https://api.intellivoid.net/intellivoid/auth/coa"):
        self.endpoint = endpoint

    def _send(self, path, **payload):
        response = requests.post("{}/{}".format(self.endpoint, path), payload)
        request_id = None
        if "x-request-id" in response.headers:
            request_id = response.headers["x-request-id"]
        return exception.CrossOverAuthenticationError.parse_and_raise(response.status_code,
                                                                      response.text,
                                                                      request_id)

    def request_authentication(self, application_id, **parameters):
        parameters["application_id"] = application_id
        return self._send("request_authentication", **parameters)["results"]

    def get_access_token(self, application_id, secret_key, request_token, poll_results=True, **parameters):
        parameters["application_id"] = application_id
        parameters["secret_key"] = secret_key,
        parameters["request_token"] = request_token

        if poll_results:
            while True:
                try:
                    return self._send("get_access_token", **parameters)["results"]
                except exception.AwaitingAuthenticationError:
                    # We're waiting for the user to authenticate
                    pass
        return self._send("get_access_token", **parameters)["results"]
