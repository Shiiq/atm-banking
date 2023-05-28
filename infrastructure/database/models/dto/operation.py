from datetime import date, datetime
from typing import Optional

from pydantic import PositiveInt

from infrastructure.database.models.constants import (BankOperationsToDB,
                                                      BankOperationsFromInput)
from .customer import CustomerInput
from ._base import DTO, FrozenDTO


class OperationInput(DTO):
    """Bank operation input model"""

    type_: BankOperationsFromInput
    amount: Optional[PositiveInt] = None
    since: Optional[date] = None
    till: Optional[date] = None


class BankOperationCreate(FrozenDTO):
    """Bank operation model to write to DB"""

    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationsToDB


class BankOperationRead(FrozenDTO):
    """Bank operation output model from DB"""

    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationsToDB
    created_at: datetime


class BankOperationSearch(DTO):
    """Bank operation search data model"""

    id: Optional[int] = None
    bank_account_id: Optional[int] = None
    bank_customer_id: Optional[int] = None
    bank_operation_type: Optional[BankOperationsToDB] = None
    since: Optional[date] = None
    till: Optional[date] = None
