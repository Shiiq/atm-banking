from datetime import datetime

from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from ._base import FrozenDTO


class Period(FrozenDTO):

    since: datetime
    till: datetime


class SummaryOperationInfo(FrozenDTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead


class BankOperationsInfo(FrozenDTO):

    customer: BankCustomerRead
    # since: datetime
    # till: datetime
    # period: Period
    operations: list[BankOperationRead]
