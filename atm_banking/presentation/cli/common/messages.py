
_BANK_STATEMENT_FORMAT_MSG = (
    "<command[bankstatement]> "
    "<your first name> <your last name> "
    "<since[DD-MM-YYYY]> <till[DD-MM-YYYY]>\n"
)

_DEPOSIT_OR_WITHDRAW_FORMAT_MSG = (
    "<command[deposit or withdraw]> "
    "<your first name> <your last name> <amount>\n"
)

REQUESTING_MSG = "Please enter your request >>> "

OPERATION_SUCCESS_MSG = "The operation was completed successfully"

WELCOME_MSG = (
    "\n"
    "Please input your request in the format:\n"
    f"{_DEPOSIT_OR_WITHDRAW_FORMAT_MSG}"
    "Or if you need a bank statement, then enter the request in the format:\n"
    f"{_BANK_STATEMENT_FORMAT_MSG}"
    "For exit input <exit>."
    "\n\n"
)


__all__ = (
    "REQUESTING_MSG",
    "OPERATION_SUCCESS_MSG",
    "WELCOME_MSG",
)
