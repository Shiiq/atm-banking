from datetime import date
from enum import StrEnum

from pydantic import Field, PositiveInt

from .base import FrozenDTO


class BankOperationsFromInput(StrEnum):

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


class BankStatementInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationsFromInput = Field(
        default=BankOperationsFromInput.BANK_STATEMENT
    )
    since: date
    till: date


class DepositInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationsFromInput = Field(
        default=BankOperationsFromInput.DEPOSIT
    )
    amount: PositiveInt


class WithdrawInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationsFromInput = Field(
        default=BankOperationsFromInput.WITHDRAW
    )
    amount: PositiveInt
