

EXIT_MESSAGE = "Work with the ATM is completed\n"

WRONG_OPERATION_MESSAGE = (
    "Invalid operation, please enter your request again, or enter <Exit>\n"
)

INCORRECT_DATA_MESSAGE = (
    "Incorrect data has been entered, please repeat your request\n"
)

REQUESTING_MESSAGE = "Please enter your request >>> "

BANK_STATEMENT_FORMAT_MESSAGE = (
    "<operation[deposit or withdraw] first_name last_name amount>\n"
)

DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE = (
    "<operation[deposit or withdraw] first_name last_name amount>\n"
)

WELCOME_MESSAGE = (
    f"Please input your request in the format\n"
    f"{DEPOSIT_OR_WITHDRAW_FORMAT_MESSAGE}"
    "Or if you need a bank statement, then enter the request in the format\n"
    f"{BANK_STATEMENT_FORMAT_MESSAGE}"
    "For exit input <exit>.\n\n"
)
