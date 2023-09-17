# messages for the cli app


_BANK_STATEMENT_FORMAT_MESSAGE = (
    "bank statement <first name> <last name> "
    "<since[DD-MM-YYYY]> <till[DD-MM-YYYY]>\n"
)

_DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE = (
    "<[deposit or withdraw] first name last name amount>\n"
)

REQUESTING_MESSAGE = "Please enter your request >>> "

OPERATION_SUCCESS_MESSAGE = "The operation was completed successfully"

WELCOME_MESSAGE = (
    "\n"
    f"Please input your request in the format:\n"
    f"{_DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE}"
    "Or if you need a bank statement, then enter the request in the format:\n"
    f"{_BANK_STATEMENT_FORMAT_MESSAGE}"
    "For exit input <exit>.\n\n"
)

__all__ = (
    "REQUESTING_MESSAGE",
    "OPERATION_SUCCESS_MESSAGE",
    "WELCOME_MESSAGE",
)
