

BANK_STATEMENT_FORMAT_MESSAGE = (
    "<bank statement first name last name since[DD-MM-YYYY] till[DD-MM-YYYY]>\n"
)

DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE = (
    "<[deposit or withdraw] first name last name amount>\n"
)

EXIT_MESSAGE = "Work with the ATM is completed\n"

INCORRECT_DATA_MESSAGE = (
    "Incorrect data has been entered, please repeat your request\n"
)

REQUESTING_MESSAGE = "Please enter your request >>> "

WELCOME_MESSAGE = (
    f"Please input your request in the format:\n"
    f"{DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE}"
    "Or if you need a bank statement, then enter the request in the format:\n"
    f"{BANK_STATEMENT_FORMAT_MESSAGE}"
    "For exit input <exit>.\n\n"
)

WRONG_OPERATION_MESSAGE = (
    "Invalid operation, please enter your request again, or enter <Exit>\n"
)

__all__ = (
    # "BANK_STATEMENT_FORMAT_MESSAGE",
    # "DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE",
    "EXIT_MESSAGE",
    "INCORRECT_DATA_MESSAGE",
    "REQUESTING_MESSAGE",
    "WELCOME_MESSAGE",
    "WRONG_OPERATION_MESSAGE",
)
