from common.database.models.constants import BankOperationsFromInput
from .customer import CustomerInput
from .operation import OperationInput
from ._base import DTO


class DepositInput(DTO):
    customer: CustomerInput
    operation: OperationInput = OperationInput(
        type_=BankOperationsFromInput.DEPOSIT
    )


class BankStatementInput(DTO):
    customer: CustomerInput
    operation: OperationInput = OperationInput(
        type_=BankOperationsFromInput.BANK_STATEMENT
    )


class WithdrawInput(DTO):
    customer: CustomerInput
    operation: OperationInput = OperationInput(
        type_=BankOperationsFromInput.WITHDRAW
    )
