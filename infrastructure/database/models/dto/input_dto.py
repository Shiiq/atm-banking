from datetime import date

from pydantic import PositiveInt, validator, ValidationError

from infrastructure.database.models.constants import BankOperationsFromInput
from ._base import FrozenDTO


class BankStatementInput(FrozenDTO):
    first_name: str
    last_name: str
    operation_type: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    since: date
    till: date


class DepositInput(FrozenDTO):
    first_name: str
    last_name: str
    operation_type: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    amount: PositiveInt


class WithdrawInput(FrozenDTO):
    first_name: str
    last_name: str
    operation_type: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
    amount: PositiveInt
