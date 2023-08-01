

class CLIAppException(Exception):
    """Base class for CLI app exception"""


class WrongOperationError(CLIAppException):

    def __init__(self, msg: str):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    def __str__(self):
        return self.msg


class ExitOperation(CLIAppException):

    def __init__(self, msg: str):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    def __str__(self):
        return self.msg
