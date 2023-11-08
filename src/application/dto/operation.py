from datetime import date, datetime, time
from typing import Optional
from uuid import UUID

from pydantic import Field, PositiveInt, field_validator

from .base import BankOperationType, DTO, FrozenDTO


class BankOperationCreate(FrozenDTO):
    """Bank operation model for creating"""

    amount: PositiveInt
    bank_account_id: UUID
    bank_customer_id: UUID
    bank_operation_type: BankOperationType


class BankOperationRead(FrozenDTO):
    """Bank operation output model from DB"""

    id: UUID
    amount: PositiveInt
    bank_account_id: UUID
    bank_customer_id: UUID
    bank_operation_type: BankOperationType
    created_at: datetime


class BankOperationSearch(DTO):
    """Bank operation search data model"""

    id: Optional[UUID] = Field(default=None)
    bank_account_id: Optional[UUID] = Field(default=None)
    bank_customer_id: Optional[UUID] = Field(default=None)
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
