from pydantic import validator, root_validator

from infrastructure.database.models.constants import BankOperationsFromInput
from .customer import CustomerInput
from .operation import OperationInput
from ._base import DTO


class BankStatementInput(DTO):
    customer: CustomerInput
    operation: OperationInput = OperationInput(
        type_=BankOperationsFromInput.BANK_STATEMENT
    )
    @root_validator
    def validate_fields_interval(cls, values):
        print(50*"#", "INVOKED BANK STATEMENT")
        print(values)
        # if values.get("operation").type_ == BankOperationsFromInput.BANK_STATEMENT:
        #     if values.get("since") > values.get("till"):
        #         raise ValueError("123")
        return values

class DepositInput(DTO):
    customer: CustomerInput
    operation: OperationInput = OperationInput(
        type_=BankOperationsFromInput.DEPOSIT
    )


class WithdrawInput(DTO):
    customer: CustomerInput
    operation: OperationInput = OperationInput(
        type_=BankOperationsFromInput.WITHDRAW
    )
