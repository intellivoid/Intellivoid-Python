class ApplicationSettingsError(Exception):

    def __init__(self, status_code, content, request_id, response):
        """
        ApplicationSettingsError Public Constructor

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
    def parse_and_raise(status_code, content, request_id, response):
        """
        Attempts to parse the response object, if it's an error then it will raise
        the appropriate exception

        :param status_code:
        :param content:
        :param request_id:
        :param response:
        :return:
        """

        if content["success"] is False:
            if "error" in content and "error_code" in content["error"]:
                raise _mapping.get(content["error"]["error_code"],
                                   ApplicationSettingsError)(status_code, content, request_id, response)
            else:
                raise ApplicationSettingsError(status_code, None, request_id, response)
        return content


class MissingParameterType(ApplicationSettingsError):
    """
    The server was expecting the parameter ‘type’ which was not provided by the client
    """

    pass


class InvalidVariableType(ApplicationSettingsError):
    """
    This error can be a generic error, see the error message for more details
    """

    pass


class MissingParameterName(ApplicationSettingsError):
    """
    The server was expecting the parameter ‘name’ which was not provided by the client
    """

    pass


class MissingParameterValue(ApplicationSettingsError):
    """
    The server was expecting the parameter ‘value’ which was not provided by the client
    """

    pass


class VariableNameEmpty(ApplicationSettingsError):
    """
    The parameter ‘name’ cannot be empty
    """

    pass


class VariableAlreadyExists(ApplicationSettingsError):
    """
    The server is refusing to overwrite an existing variable because the parameter “overwrite” was enabled
    """

    pass


class InvalidJsonDataInValue(ApplicationSettingsError):
    """
    The server was expecting JSON data in the ‘value’ parameter but couldn’t parse
    """

    pass


class InvalidDataInValue(ApplicationSettingsError):
    """
    This error is returned when there is invalid data in the ‘value’ parameter which is not applicable to the data
    type, the message will contain more information about the error
    """

    pass


class MaximumApplicationSizeExceeded(ApplicationSettingsError):
    """
    The changes cannot be made because the maximum size for this Application’s storage for settings/variables has
    exceeded. You need to remove data to free up space
    """

    pass


class VariableNotFound(ApplicationSettingsError):
    """
    The requested variable does not exist in the current context
    """

    pass


class AppendNotApplicable(ApplicationSettingsError):
    """
    The server refuses to append data to this variable type because it’s not supported, only list and arrays are
    supported
    """

    pass


class InvalidByValue(ApplicationSettingsError):
    """
    The parameter ‘by’ only accepts “index” or “key” as values
    """

    pass


class DeleteNotApplicableInVariableType(ApplicationSettingsError):
    """
    The server is refusing to delete data from a variable because it’s only applicable to List & Array types
    """

    pass


class CannotRemoveValueByIndex(ApplicationSettingsError):
    """
    You can’t delete data by index on a array data type since arrays are a key and value pair
    """

    pass


_mapping = {
    1: MissingParameterType,
    2: InvalidVariableType,
    3: MissingParameterName,
    4: MissingParameterValue,
    5: VariableNameEmpty,
    6: VariableAlreadyExists,
    7: InvalidJsonDataInValue,
    8: InvalidDataInValue,
    9: MaximumApplicationSizeExceeded,
    10: VariableNotFound,
    11: AppendNotApplicable,
    12: InvalidByValue,
    13: DeleteNotApplicableInVariableType,
    14: CannotRemoveValueByIndex
}
