from enum import StrEnum


WELCOME_MESSAGE = ("Please input your request in the format "
                   "<operation[deposit or withdraw] first_name last_name amount>.\n"
                   "Or if you need a bank statement, then enter the request in the format "
                   "<bank_statement first_name last_name since till>.\n\n")

EXITING_MESSAGE = ("Work with the ATM is completed.")


class BankOperationsFromInput(StrEnum):
    """Possible bank operations to choose from CLI or API"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


class ExitCommand(StrEnum):
    """Exit command."""
    EXIT = "exit"
