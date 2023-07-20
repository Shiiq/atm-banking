from enum import StrEnum


class BankOperationsToDB(StrEnum):
    """Bank operations to write to DB"""

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
