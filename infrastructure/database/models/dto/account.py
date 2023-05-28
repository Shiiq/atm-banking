from datetime import date, datetime
from typing import Optional

from pydantic import NonNegativeInt

from ._base import DTO, FrozenDTO


class BankAccountCreate(FrozenDTO):
    """Bank account model to write to DB"""

    balance: NonNegativeInt = 0


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

    id: Optional[int] = None
    customer_id: Optional[int] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
