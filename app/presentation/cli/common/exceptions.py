

class CLIAppException(Exception):
    """Base class for CLI app exception"""
    pass


class ExitOperation(CLIAppException):

    def __init__(self, msg: str):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    def __str__(self):
        return self.msg


class InputDataError(CLIAppException):

    def __init__(self, msg):
        self._msg = msg

    @property
    def msg(self):
        return

    def __str__(self):
        return self.msg


class ValidateDataError(CLIAppException):

    def __init__(self, errors_data: list):
        self._errors_data = errors_data[0]

    @property
    def msg(self):
        return (f"An error '{self._errors_data['msg']}' has occured. "
                f"Please input in '{self._errors_data['loc']}' fields correct data.")

    def __str__(self):
        return self.msg


class WrongOperationError(CLIAppException):

    def __init__(self, msg: str):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    def __str__(self):
        return self.msg
