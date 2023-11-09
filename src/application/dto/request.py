from datetime import date

from pydantic import Field, PositiveInt

from .base import BankOperationType, FrozenDTO

MIN_AMOUNT = 0
MAX_TO_DEPOSIT = 10_000_000
MAX_TO_WITHDRAW = 5_000_000


class BankStatementRequest(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = BankOperationType.BANK_STATEMENT
    since: date
    till: date


class DepositRequest(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = BankOperationType.DEPOSIT
    amount: PositiveInt = Field(gt=MIN_AMOUNT, le=MAX_TO_DEPOSIT)


class WithdrawRequest(FrozenDTO):

    first_name: str
    last_name: str
    operation_type: BankOperationType = BankOperationType.WITHDRAW
    amount: PositiveInt = Field(gt=MIN_AMOUNT, le=MAX_TO_WITHDRAW)
