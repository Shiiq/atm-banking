from datetime import date

from pydantic import PositiveInt

from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from .base import FrozenDTO
from .input import BankOperationsFromInput


# class _BankOperationsInfo(FrozenDTO):
#
#     since: date
#     till: date
#     first_name: str
#     last_name: str
#     operations: list[BankOperationRead]
#
#
# class _SummaryOperationInfo(FrozenDTO):
#
#     first_name: str
#     last_name: str
#     operation: BankOperationsFromInput
#     amount: PositiveInt


class SummaryOperationInfo(FrozenDTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead


class BankOperationsInfo(FrozenDTO):

    since: date
    till: date
    customer: BankCustomerRead
    operations: list[BankOperationRead]
