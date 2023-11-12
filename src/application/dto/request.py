from datetime import date

from pydantic import Field, PositiveInt

from src.application.common import CUSTOMER_NAME_PATTERN
from src.application.common import MIN_AMOUNT
from src.application.common import MAX_AMOUNT_TO_DEPOSIT
from src.application.common import MAX_AMOUNT_TO_WITHDRAW
from .base import BankOperationType, FrozenDTO


class BankStatementRequest(FrozenDTO):

    first_name: str = Field(pattern=CUSTOMER_NAME_PATTERN)
    last_name: str = Field(pattern=CUSTOMER_NAME_PATTERN)
    operation_type: BankOperationType = BankOperationType.BANK_STATEMENT
    since: date
    till: date


class DepositRequest(FrozenDTO):

    first_name: str = Field(pattern=CUSTOMER_NAME_PATTERN)
    last_name: str = Field(pattern=CUSTOMER_NAME_PATTERN)
    operation_type: BankOperationType = BankOperationType.DEPOSIT
    amount: PositiveInt = Field(gt=MIN_AMOUNT, le=MAX_AMOUNT_TO_DEPOSIT)


class WithdrawRequest(FrozenDTO):

    first_name: str = Field(pattern=CUSTOMER_NAME_PATTERN)
    last_name: str = Field(pattern=CUSTOMER_NAME_PATTERN)
    operation_type: BankOperationType = BankOperationType.WITHDRAW
    amount: PositiveInt = Field(gt=MIN_AMOUNT, le=MAX_AMOUNT_TO_WITHDRAW)
