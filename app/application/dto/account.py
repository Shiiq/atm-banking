from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, NonNegativeInt

from .base import DTO, FrozenDTO

DEFAULT_BALANCE = 0


class BankAccountCreate(FrozenDTO):
    """Bank account model to write to DB"""

    balance: NonNegativeInt = Field(default=DEFAULT_BALANCE)


class BankAccountRead(FrozenDTO):
    """Bank account output model from DB"""

    id: UUID
    balance: NonNegativeInt
    created_at: datetime
    updated_at: datetime


class BankAccountUpdate(DTO):
    """Bank account update data model"""

    id: UUID
    balance: NonNegativeInt


class BankAccountSearch(DTO):
    """Bank account search data model"""

    id: Optional[UUID] = Field(default=None)
    customer_id: Optional[UUID] = Field(default=None)
    created_at: Optional[date] = Field(default=None)
    updated_at: Optional[date] = Field(default=None)
