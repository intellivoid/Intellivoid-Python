from .coa.exceptions import CrossOverAuthenticationError
from .application.settings_exceptions import ApplicationSettingsError

__all__ = ["ServiceException"]

"""
This file is for handling multiple exception types by parsing the response and raising the correct
exception. The API can return multiple errors for multiple things, this class is designed to figure
out what caused the error and raise it's appropriate exceptions.

This could be improved in the future
"""

import json


class ServiceException(Exception):

    def __init__(self, status_code, content, request_id, response):
        """
        ServiceException Public Constructor

        :param status_code:
        :param content:
        :param request_id:
        :param response:
        """
        self.status_code = status_code
        self.content = content
        self.response = response
        self.request_id = request_id
        self.message = None
        self.error_code = None
        self.type = None

        # This part can be improved
        if content is not None:
            self.message = content["error"]["message"]
            self.error_code = content["error"]["error_code"]
            self.type = content["error"]["type"]

        super().__init__(self.message or content)

    @staticmethod
    def parse_and_raise(status_code, response, request_id):
        """
        Parses the response and detects the error type

        :param status_code:
        :param response:
        :param request_id:
        :return:
        """

        try:
            content = json.loads(response)
        except json.decoder.JSONDecodeError:
            raise ServiceException(status_code, None, request_id, response)

        # Parse the response
        if content["success"] is False:
            # Check if the type is available
            if "error" in content and "type" in content["error"]:

                # COA Exception handler
                if content["error"]["type"].lower() == "coa":
                    CrossOverAuthenticationError.parse_and_raise(status_code, content, request_id, response)

                if content["error"]["type"].lower() == "settings":
                    ApplicationSettingsError.parse_and_raise(status_code, content, request_id, response)

                if content["error"]["type"].lower() == "server":
                    raise _mapping.get(content["error"]["error_code"],
                                       ServiceException)(status_code, content, request_id, response)

            # If detecting the type fails, it's a generic error
            raise ServiceException(status_code, content, request_id, response)

        return content


class InternalServerError(ServiceException):
    """
    An unexpected internal server error, this incident should be reported to support
    """

    pass


class ServiceError(ServiceException):
    """
    This error can be a generic error, see the error message for more details
    """

    pass


_mapping = {
    -1: InternalServerError,
    0: ServiceError
}
