from datetime import date

from pydantic import PositiveInt, NegativeInt

from common.database.models.constants import BankOperationsFromInput

from .customer import CustomerInputDTO
from ._base import DTO


class BankStatementInputDTO(DTO):
    customer: CustomerInputDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    since: date
    till: date


class DepositInputDTO(DTO):
    customer: CustomerInputDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    amount: PositiveInt


class WithdrawInputDTO(DTO):
    customer: CustomerInputDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
    amount: NegativeInt

