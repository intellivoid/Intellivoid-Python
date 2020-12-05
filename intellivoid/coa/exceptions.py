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

import json

__all__ = ["CrossOverAuthenticationError"]


class CrossOverAuthenticationError(Exception):

    def __init__(self, status_code, content, request_id):
        """
        CrossOverAuthenticationError Public Constructor

        :param status_code:
        :param content:
        :param request_id:
        """
        self.status_code = status_code
        self.content = content
        self.request_id = request_id
        self.error_code = content["error"]["error_code"]
        self.message = content["error"]["message"]
        self.type = content["error"]["type"]
        super().__init__(self.message or content)

    @staticmethod
    def parse_and_raise(status_code, response, request_id):
        """
        Attempts to parse the response object, if it's an error then it will raise
        the appropriate exception

        :param status_code:
        :param response:
        :param request_id:
        :return:
        """

        if response["success"] is False:
            if "error" in response and "error_code" in response["error"]:
                raise _mapping.get(response["error"]["error_code"],
                                   CrossOverAuthenticationError)(status_code, response, request_id)
            else:
                raise CrossOverAuthenticationError(status_code, "", request_id)
        return response


class AccessDeniedSecurityIssue(CrossOverAuthenticationError):
    """
    The service provider may deny access to a users account when it believes the user’s security is at risk and the
    user must review their account in order to fix this issue, this can range from Government-backed attacks to a
    compromised account
    """

    pass


class AwaitingAuthentication(CrossOverAuthenticationError):
    """
    This isn’t an error, but rather a status-type error which indicates that the service provider is waiting for the
    user to authenticate. This will eventually result in an access token being granted or the request token being
    expired. The client should poll this request until a result has been returned.
    """

    pass


class InvalidRequestToken(CrossOverAuthenticationError):
    """
    This error is raised when the client provides an invalid Request Token
    """

    pass


class MissingParameterRequestToken(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘request_token’ parameter.
    """

    pass


class UnsupportedApplicationAuthenticationType(CrossOverAuthenticationError):
    """
    The service provider no longer supports this Application Authentication Type and the administrator of this
    Application must update their Authentication Type and their client to support it
    """

    pass


class RequestTokenExpired(CrossOverAuthenticationError):
    """
    Due to user inactivity, the request token has expired and the Application must request authentication again
    """

    pass


class UserRevokedAccess(CrossOverAuthenticationError):
    """
    The user revoked access to the Application, the Application must request authentication again.
    """

    pass


class AccountSuspended(CrossOverAuthenticationError):
    """
    The user’s account has been suspended by the service provider and is no longer available
    """

    pass


class AccessTokenExpired(CrossOverAuthenticationError):
    """
    The Access Token has expired due to lack of activity, the client must request authentication again and retrieve a
    new Access Token
    """

    pass


class AccountNotFound(CrossOverAuthenticationError):
    """
    This error happens when the account was deleted from the server either by the service provider or the user
    """

    pass


class IncorrectAccessToken(CrossOverAuthenticationError):
    """
    This error happens when the client provides an Access Token which is invalid
    """

    pass


class MissingParameterAccessTokenError(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘access_token’ parameter.
    """

    pass


class IncorrectSecretKey(CrossOverAuthenticationError):
    """
    The client’s access has been denied by the service provider for failing to provide the correct secret key that’s
    associated with the Application ID.
    """

    pass


class MissingParameterSecretKey(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘secret_key’ parameter.
    """

    pass


class InternalServerErrorWhileTryingToAuthenticateUserError(CrossOverAuthenticationError):
    """
    This error is raised when an unexpected error is raised when the service provide was trying to authenticate the
    user with your Application, this incident should be reported to support.
    """

    pass


class AlreadyAuthenticated(CrossOverAuthenticationError):
    """
    The client is attempting to generate a Authentication Access Token using a Authentication Request Token which has
    already been used to create an Authentication Access Token. This process can only be done once, if you lose the
    Authentication Access Token then you must request Authentication to the user again.
    """

    pass


class AuthenticationAccessDoesNotExist(CrossOverAuthenticationError):
    """
    The client provided an Authentication Access Token which does not exist with the service provider
    """

    pass


class InvalidRedirectUrl(CrossOverAuthenticationError):
    """
    This error raises when the client provides a ‘redirect’ parameter containing a value that is not a valid URL. For
    example (https://example.com/) is valid but (foobar) is not.
    """

    pass


class MissingParameterRedirect(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘redirect’ parameter when trying to request
    authentication to an Application that uses the “Redirect” authentication method
    """

    pass


class ApplicationUnavailable(CrossOverAuthenticationError):
    """
    The Application is currently unavailable either from the service provider or the owner of this Application
    """

    pass


class ApplicationSuspended(CrossOverAuthenticationError):
    """
    The Application is suspended by the service provider
    """

    pass


class InvalidApplicationId(CrossOverAuthenticationError):
    """
    This error is raised when the client provides a Application ID that isn’t valid
    """

    pass


class MissingParameterApplicationId(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘application_id’ parameter.
    """

    pass


class InternalServerError(CrossOverAuthenticationError):
    """
    An unexpected server error occurred, this may be a bug. These types of errors could be fixed and or not; it
    should be reported to support
    """

    pass


class InsufficientPermissions(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘application_id’ parameter.
    """

    pass


_mapping = {
    -1: InternalServerError,
    1: MissingParameterApplicationId,
    2: InvalidApplicationId,
    3: ApplicationSuspended,
    4: ApplicationUnavailable,
    6: MissingParameterRedirect,
    16: InvalidRedirectUrl,
    19: AuthenticationAccessDoesNotExist,
    20: AlreadyAuthenticated,
    21: InternalServerErrorWhileTryingToAuthenticateUserError,
    22: MissingParameterSecretKey,
    23: IncorrectSecretKey,
    24: MissingParameterAccessTokenError,
    25: IncorrectAccessToken,
    26: AccountNotFound,
    27: AccessTokenExpired,
    28: AccountSuspended,
    29: UserRevokedAccess,
    30: InsufficientPermissions,
    34: RequestTokenExpired,
    35: UnsupportedApplicationAuthenticationType,
    39: MissingParameterRequestToken,
    40: InvalidRequestToken,
    41: AwaitingAuthentication,
    51: AccessDeniedSecurityIssue
}
