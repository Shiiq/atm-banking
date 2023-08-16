from datetime import date
from enum import StrEnum

from pydantic import Field, PositiveInt

from .base import FrozenDTO


class BankOperationType(StrEnum):

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


class BankStatementInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = Field(
        default=BankOperationType.BANK_STATEMENT
    )
    since: date
    till: date


class DepositInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = Field(
        default=BankOperationType.DEPOSIT
    )
    amount: PositiveInt


class WithdrawInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = Field(
        default=BankOperationType.WITHDRAW
    )
    amount: PositiveInt
