from datetime import datetime
from typing import Optional

from pydantic import PositiveInt, validator, ValidationError

from infrastructure.database.models.constants import BankOperationsToDB
from ._base import DTO, FrozenDTO


class BankOperationCreate(FrozenDTO):
    """Bank operation model to write to DB"""

    amount: PositiveInt
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationsToDB


class BankOperationRead(FrozenDTO):
    """Bank operation output model from DB"""

    id: int
    amount: PositiveInt
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
    since: Optional[datetime] = None
    till: Optional[datetime] = None

    @validator("till")
    def adding_hours_to_till(cls, value):
        value = value.replace(hour=23, minute=59)
        return value
