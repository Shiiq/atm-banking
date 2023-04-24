from enum import StrEnum


class BankOperationsFromInput(StrEnum):
    """Possible bank operations to choose from CLI or API"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


class BankOperationsToDB(StrEnum):
    """Bank operations to write to database"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
