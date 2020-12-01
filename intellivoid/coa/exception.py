import json

__all__ = ["CrossOverAuthenticationError"]


class CrossOverAuthenticationError(Exception):

    def __init__(self, status_code, content, request_id):
        self.status_code = status_code
        self.content = content
        self.request_id = request_id
        self.message = content.get("message", None) if content else "Unknown"
        self.error_code = content.get("error_code", None) if content else "Unknown"
        super().__init__(self.message or content)

    @staticmethod
    def parse_and_raise(status_code, content, request_id):
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
    pass


class AwaitingAuthenticationError(CrossOverAuthenticationError):
    pass


class InvalidRequestTokenError(CrossOverAuthenticationError):
    pass


class MissingParameterRequestTokenError(CrossOverAuthenticationError):
    pass


class UnsupportedApplicationAuthenticationTypeError(CrossOverAuthenticationError):
    pass


class RequestTokenExpiredError(CrossOverAuthenticationError):
    pass


class AccessDeniedUserDisabledAccessError(CrossOverAuthenticationError):
    pass


class AccountSuspendedError(CrossOverAuthenticationError):
    pass


class AccessTokenExpiredError(CrossOverAuthenticationError):
    pass


class AccessDeniedAccountNotFoundError(CrossOverAuthenticationError):
    pass


class AccessDeniedIncorrectAccessTokenError(CrossOverAuthenticationError):
    pass


class MissingParameterAccessTokenError(CrossOverAuthenticationError):
    pass


class AccessDeniedIncorrectSecretKeyError(CrossOverAuthenticationError):
    pass


class MissingParameterSecretKeyError(CrossOverAuthenticationError):
    pass


class InternalServerErrorWhileTryingToAuthenticateUserError(CrossOverAuthenticationError):
    pass


class AlreadyAuthenticatedError(CrossOverAuthenticationError):
    pass


class AuthenticationAccessDoesNotExistError(CrossOverAuthenticationError):
    pass


class InvalidRedirectUrlError(CrossOverAuthenticationError):
    pass


class MissingParameterRedirectError(CrossOverAuthenticationError):
    pass


class ApplicationUnavailableError(CrossOverAuthenticationError):
    pass


class ApplicationSuspendedError(CrossOverAuthenticationError):
    pass


class InvalidApplicationIdError(CrossOverAuthenticationError):
    pass


class MissingParameterApplicationIdError(CrossOverAuthenticationError):
    pass


class InternalServerError(CrossOverAuthenticationError):
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
