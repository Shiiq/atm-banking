from datetime import date, datetime
from typing import Optional

from pydantic import Field, NonNegativeInt

from ._base import DTO, FrozenDTO


class BankAccountCreate(FrozenDTO):
    """Bank account model to write to DB"""

    balance: NonNegativeInt = Field(default=0)


class BankAccountRead(FrozenDTO):
    """Bank account output model from DB"""

    id: int
    balance: NonNegativeInt
    created_at: datetime
    updated_at: datetime


class BankAccountUpdate(DTO):
    """Bank account update data model"""

    id: int
    balance: NonNegativeInt


class BankAccountSearch(DTO):
    """Bank account search data model"""

    id: Optional[int] = Field(default=None)
    customer_id: Optional[int] = Field(default=None)
    created_at: Optional[date] = Field(default=None)
    updated_at: Optional[date] = Field(default=None)
