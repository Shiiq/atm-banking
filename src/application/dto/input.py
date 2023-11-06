from datetime import date

from pydantic import Field, PositiveInt

# from src.application.dto import BankOperationType
from .base import BankOperationType, FrozenDTO

MIN_AMOUNT = 0
MAX_TO_DEPOSIT = 10_000_000
MAX_TO_WITHDRAW = 5_000_000


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
    amount: PositiveInt = Field(gt=MIN_AMOUNT, le=MAX_TO_DEPOSIT)


class WithdrawInput(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = Field(
        default=BankOperationType.WITHDRAW
    )
    amount: PositiveInt = Field(gt=MIN_AMOUNT, le=MAX_TO_WITHDRAW)
