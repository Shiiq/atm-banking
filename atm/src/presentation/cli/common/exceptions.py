from src.application.common import MAX_AMOUNT_TO_DEPOSIT
from src.application.common import MAX_AMOUNT_TO_WITHDRAW

_EXIT_MSG = "Work with the ATM is completed\n"

_INCORRECT_DATA_MSG = (
    "Incorrect data has been entered, please repeat your request.\n"
    "Your first and last name must not contain numbers.\n"
    f"Maximum amount to top up a bank account is {MAX_AMOUNT_TO_DEPOSIT}, "
    f"and for withdrawal is {MAX_AMOUNT_TO_WITHDRAW}.\n"
)

_UNKNOWN_OPERATION_MSG = (
    "Unknown operation, please repeat your request, or enter <exit>\n"
)

_RUNTIME_ERROR_MSG = "The application is already running"


class CLIAppException(Exception):
    """Base class for CLI app exception"""

    pass


class CLIAppRuntimeError(CLIAppException):

    _msg = _RUNTIME_ERROR_MSG

    @property
    def ui_msg(self):
        return self._msg

    def __str__(self):
        return self._msg


class ExitOperation(CLIAppException):

    _msg = _EXIT_MSG

    @property
    def ui_msg(self):
        return self._msg


class InputDataError(CLIAppException):

    _msg = _INCORRECT_DATA_MSG

    @property
    def ui_msg(self):
        return self._msg


class UnknownOperationError(CLIAppException):

    _msg = _UNKNOWN_OPERATION_MSG

    @property
    def ui_msg(self):
        return self._msg


__all__ = (
    "CLIAppRuntimeError",
    "ExitOperation",
    "InputDataError",
    "UnknownOperationError",
)
