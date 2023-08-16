from datetime import date, datetime, time
from typing import Optional

from pydantic import Field, PositiveInt, field_validator

from app.infrastructure.database.models.constants import BankOperationsDB
from .base import DTO, FrozenDTO
from .input import BankOperationType


class BankOperationCreate(FrozenDTO):
    """Bank operation model to write to DB"""

    amount: PositiveInt
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationType


class BankOperationRead(FrozenDTO):
    """Bank operation output model from DB"""

    id: int
    amount: PositiveInt
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationType
    created_at: datetime


class BankOperationSearch(DTO):
    """Bank operation search data model"""

    id: Optional[int] = Field(default=None)
    bank_account_id: Optional[int] = Field(default=None)
    bank_customer_id: Optional[int] = Field(default=None)
    bank_operation_type: Optional[BankOperationType] = Field(default=None)
    since: Optional[datetime] = Field(default=None)
    till: Optional[datetime] = Field(default=None)

    @field_validator("since", mode="before")
    def convert_since_to_datetime(cls, d: date) -> datetime:
        t = time(hour=0, minute=0, second=0, microsecond=0)
        return datetime.combine(d, t)

    @field_validator("till", mode="before")
    def convert_till_to_datetime(cls, d: date) -> datetime:
        t = time(hour=23, minute=59, second=59, microsecond=999999)
        return datetime.combine(d, t)
