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

# This file is for handling multiple exception types by parsing the response and raising the correct
# exception. The API can return multiple errors for multiple things, this class is designed to figure
# out what caused the error and raise its appropriate exceptions.
# This could be improved in the future


from intellivoid.sync.coa.exceptions import CrossOverAuthenticationError
from intellivoid.sync.application.exceptions import ApplicationSettingsError
import json


__all__ = ["ServiceException"]


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
