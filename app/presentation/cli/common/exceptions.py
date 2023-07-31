

class CLIAppException(Exception):
    """Base CLI app exception"""


class WrongOperationError(CLIAppException):

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self.message


class ExitOperation(CLIAppException):

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self.message
