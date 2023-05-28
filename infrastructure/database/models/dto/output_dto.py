from datetime import date

from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from ._base import FrozenDTO


class Period(FrozenDTO):

    since: date
    till: date


class SummaryOperationInfo(FrozenDTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead


class BankOperationsInfo(FrozenDTO):

    customer: BankAccountRead
    period: Period
    operations: list[BankOperationRead]
