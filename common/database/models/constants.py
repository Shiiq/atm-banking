from enum import StrEnum


class BankOperationsToDB(StrEnum):
    """Bank operations to write to DB"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class BankOperationsFromInput(StrEnum):
    """Possible bank operations"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"
