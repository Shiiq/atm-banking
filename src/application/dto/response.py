from datetime import date, datetime
from typing import Optional

from pydantic import Field, PositiveInt, NonNegativeInt

from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from .base import BankOperationType, FrozenDTO


class OperationShortResponse(FrozenDTO):
    """Output data model with short operation information."""

    operation_datetime: datetime = Field(
        validation_alias="created_at"
    )
    operation_type: BankOperationType = Field(
        validation_alias="bank_operation_type"
    )
    operation_amount: PositiveInt = Field(
        validation_alias="amount"
    )
    current_balance: Optional[NonNegativeInt] = None


class OperationFullResponse(FrozenDTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead


class BankStatementShortResponse(FrozenDTO):
    """Output data model with short bank statement information."""

    since: date
    till: date
    balance: NonNegativeInt
    operations: list[OperationShortResponse]


class BankStatementFullResponse(FrozenDTO):

    since: date
    till: date
    customer: BankCustomerRead
    operations: list[BankOperationRead]
