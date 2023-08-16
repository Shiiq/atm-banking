from enum import StrEnum


class BankOperationsDB(StrEnum):
    """Bank operations to read/write from DB"""

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
