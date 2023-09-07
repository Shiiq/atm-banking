from datetime import date, datetime

from pydantic import PositiveInt, NonNegativeInt

from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from .input import BankOperationType
from .base import FrozenDTO


class ShortOperationInfo(FrozenDTO):

    operation_datetime: datetime
    operation_type: BankOperationType
    operation_amount: PositiveInt
    balance: NonNegativeInt


class FullOperationInfo(FrozenDTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead


class ShortBankStatementInfo(FrozenDTO):

    since: date
    till: date
    operations: list[ShortOperationInfo]


class FullBankStatementInfo(FrozenDTO):

    since: date
    till: date
    customer: BankCustomerRead
    operations: list[BankOperationRead]
