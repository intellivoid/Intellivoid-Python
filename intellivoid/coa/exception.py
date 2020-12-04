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
        self.message = content.get("message", None) if content else "Unknown"
        self.error_code = content.get("error_code", None) if content else "Unknown"
        super().__init__(self.message or content)

    @staticmethod
    def parse_and_raise(status_code, content, request_id):
        """
        Attempts to parse the request, if it's an error then it will raise
        the appropriate exception

        :param status_code:
        :param content:
        :param request_id:
        :return:
        """
        try:
            response = json.loads(content)
        except json.decoder.JSONDecodeError:
            raise CrossOverAuthenticationError(status_code, None, request_id)
        if response["success"] is False:
            if "error" in response and "error_code" in response["error"]:
                raise _mapping.get(response["error"]["error_code"],
                                   CrossOverAuthenticationError)(status_code, response, request_id)
            else:
                raise CrossOverAuthenticationError(status_code, None, request_id)
        return response


class AccessDeniedDueToSecurityIssuesError(CrossOverAuthenticationError):
    """
    The service provider may deny access to a users account when it believes the user’s security is at risk and the
    user must review their account in order to fix this issue, this can range from Government-backed attacks to a
    compromised account
    """
    pass


class AwaitingAuthenticationError(CrossOverAuthenticationError):
    """
    This isn’t an error, but rather a status-type error which indicates that the service provider is waiting for the
    user to authenticate. This will eventually result in an access token being granted or the request token being
    expired. The client should poll this request until a result has been returned.
    """
    pass


class InvalidRequestTokenError(CrossOverAuthenticationError):
    """
    This error is raised when the client provides an invalid Request Token
    """
    pass


class MissingParameterRequestTokenError(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘request_token’ parameter.
    """
    pass


class UnsupportedApplicationAuthenticationTypeError(CrossOverAuthenticationError):
    """
    The service provider no longer supports this Application Authentication Type and the administrator of this
    Application must update their Authentication Type and their client to support it
    """
    pass


class RequestTokenExpiredError(CrossOverAuthenticationError):
    """
    Due to user inactivity, the request token has expired and the Application must request authentication again
    """
    pass


class AccessDeniedUserDisabledAccessError(CrossOverAuthenticationError):
    """
    The user revoked access to the Application, the Application must request authentication again.
    """
    pass


class AccountSuspendedError(CrossOverAuthenticationError):
    """
    The user’s account has been suspended by the service provider and is no longer available
    """
    pass


class AccessTokenExpiredError(CrossOverAuthenticationError):
    """
    The Access Token has expired due to lack of activity, the client must request authentication again and retrieve a
    new Access Token
    """
    pass


class AccessDeniedAccountNotFoundError(CrossOverAuthenticationError):
    """
    This error happens when the account was deleted from the server either by the service provider or the user
    """
    pass


class AccessDeniedIncorrectAccessTokenError(CrossOverAuthenticationError):
    """
    This error happens when the client provides an Access Token which is invalid
    """
    pass


class MissingParameterAccessTokenError(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘access_token’ parameter.
    """
    pass


class AccessDeniedIncorrectSecretKeyError(CrossOverAuthenticationError):
    """
    The client’s access has been denied by the service provider for failing to provide the correct secret key that’s
    associated with the Application ID.
    """
    pass


class MissingParameterSecretKeyError(CrossOverAuthenticationError):
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


class AlreadyAuthenticatedError(CrossOverAuthenticationError):
    """
    The client is attempting to generate a Authentication Access Token using a Authentication Request Token which has
    already been used to create an Authentication Access Token. This process can only be done once, if you lose the
    Authentication Access Token then you must request Authentication to the user again.
    """
    pass


class AuthenticationAccessDoesNotExistError(CrossOverAuthenticationError):
    """
    The client provided an Authentication Access Token which does not exist with the service provider
    """
    pass


class InvalidRedirectUrlError(CrossOverAuthenticationError):
    """
    This error raises when the client provides a ‘redirect’ parameter containing a value that is not a valid URL. For
    example (https://example.com/) is valid but (foobar) is not.
    """
    pass


class MissingParameterRedirectError(CrossOverAuthenticationError):
    """
    This error is raised when the client fails to provide the required ‘redirect’ parameter when trying to request
    authentication to an Application that uses the “Redirect” authentication method
    """
    pass


class ApplicationUnavailableError(CrossOverAuthenticationError):
    """
    The Application is currently unavailable either from the service provider or the owner of this Application
    """
    pass


class ApplicationSuspendedError(CrossOverAuthenticationError):
    """
    The Application is suspended by the service provider
    """
    pass


class InvalidApplicationIdError(CrossOverAuthenticationError):
    """
    This error is raised when the client provides a Application ID that isn’t valid
    """
    pass


class MissingParameterApplicationIdError(CrossOverAuthenticationError):
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


_mapping = {
    -1: InternalServerError,
    1: MissingParameterApplicationIdError,
    2: InvalidApplicationIdError,
    3: ApplicationSuspendedError,
    4: ApplicationUnavailableError,
    6: MissingParameterRedirectError,
    16: InvalidRedirectUrlError,
    19: AuthenticationAccessDoesNotExistError,
    20: AlreadyAuthenticatedError,
    21: InternalServerErrorWhileTryingToAuthenticateUserError,
    22: MissingParameterSecretKeyError,
    23: AccessDeniedIncorrectSecretKeyError,
    24: MissingParameterAccessTokenError,
    25: AccessDeniedIncorrectAccessTokenError,
    26: AccessDeniedAccountNotFoundError,
    27: AccessTokenExpiredError,
    28: AccountSuspendedError,
    29: AccessDeniedUserDisabledAccessError,
    34: RequestTokenExpiredError,
    35: UnsupportedApplicationAuthenticationTypeError,
    39: MissingParameterRequestTokenError,
    40: InvalidRequestTokenError,
    41: AwaitingAuthenticationError,
    51: AccessDeniedDueToSecurityIssuesError
}
