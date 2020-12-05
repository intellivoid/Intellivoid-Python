from .coa.exceptions import CrossOverAuthenticationError

__all__ = ["ServiceException"]

"""
This file is for handling multiple exception types by parsing the response and raising the correct
exception. The API can return multiple errors for multiple things, this class is designed to figure
out what caused the error and raise it's appropriate exceptions.

This could be improved in the future
"""

import json


class ServiceException(Exception):

    def __init__(self, status_code, content, request_id):
        """
        ServiceException Public Constructor

        :param status_code:
        :param content:
        :param request_id:
        """
        self.status_code = status_code
        self.content = content
        self.request_id = request_id
        self.message = content["error"]["message"]
        self.error_code = content["error"]["error_code"]
        self.type = content["error"]["type"]
        super().__init__(self.message or content)

    @staticmethod
    def parse_and_raise(status_code, content, request_id):
        """
        Parses the response and detects the error type

        :param status_code:
        :param content:
        :param request_id:
        :return:
        """

        try:
            response = json.loads(content)
        except json.decoder.JSONDecodeError:
            raise ServiceException(status_code, content, request_id)  # Should it return the content too?

        # Parse the response
        if response["success"] is False:
            # Check if the type is available
            if "error" in response and "type" in response["error"]:

                # COA Exception handler
                if response["error"]["type"].lower() == "coa":
                    CrossOverAuthenticationError.parse_and_raise(status_code, response, request_id)
                    # Should it manually raise the exception here if the parse_and_raise method does nothing?

                if response["error"]["type"].lower() == "server":
                    raise _mapping.get(response["error"]["error_code"],
                                       ServiceException)(status_code, response, request_id)

            # If detecting the type fails, it's a generic error
            raise ServiceException(status_code, content, request_id)

        return response


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
