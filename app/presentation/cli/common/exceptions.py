
_EXIT_MESSAGE = "Work with the ATM is completed\n"
_INCORRECT_DATA_MESSAGE = (
    "Incorrect data has been entered, please repeat your request\n"
)
_WRONG_OPERATION_MESSAGE = (
    "Invalid operation, please enter your request again, or enter <Exit>\n"
)


class CLIAppException(Exception):
    """Base class for CLI app exception"""

    pass


class ExitOperation(CLIAppException):

    _msg = _EXIT_MESSAGE
    # def __init__(self):
    #     self._msg = _EXIT_MESSAGE

    @property
    def ui_msg(self):
        return self._msg


class InputDataError(CLIAppException):

    _msg = _INCORRECT_DATA_MESSAGE
    # def __init__(self):
    #     self._msg = _INCORRECT_DATA_MESSAGE

    @property
    def ui_msg(self):
        return self._msg


class ValidateDataError(CLIAppException):

    def __init__(self, errors_data: list):
        self._errors_data = errors_data[0]

    @property
    def msg(self):
        return (f"An error '{self._errors_data['msg']}' has occured. "
                f"Please input in '{self._errors_data['loc']}' fields correct data.")


class WrongOperationError(CLIAppException):

    _msg = _WRONG_OPERATION_MESSAGE
    # def __init__(self):
    #     self._msg = _WRONG_OPERATION_MESSAGE

    @property
    def ui_msg(self):
        return self._msg
