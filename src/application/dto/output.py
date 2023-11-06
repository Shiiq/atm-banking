from datetime import date, datetime
from typing import Optional

from pydantic import Field, PositiveInt, NonNegativeInt

# from src.application.dto import BankAccountRead
# from src.application.dto import BankCustomerRead
# from src.application.dto import BankOperationRead
# from src.application.dto import BankOperationType
from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from .base import BankOperationType, FrozenDTO


class ShortOperationInfo(FrozenDTO):

    operation_datetime: datetime = Field(
        validation_alias="created_at"
    )
    operation_type: BankOperationType = Field(
        validation_alias="bank_operation_type"
    )
    operation_amount: PositiveInt = Field(
        validation_alias="amount"
    )
    current_balance: Optional[NonNegativeInt] = Field(
        default=None
    )


class FullOperationInfo(FrozenDTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead


class ShortBankStatementInfo(FrozenDTO):

    since: date
    till: date
    balance: NonNegativeInt
    operations: list[ShortOperationInfo]


class FullBankStatementInfo(FrozenDTO):

    since: date
    till: date
    customer: BankCustomerRead
    operations: list[BankOperationRead]
