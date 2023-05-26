from datetime import date, datetime
from typing import Optional

from pydantic import NonNegativeInt

from ._base import DTO


class BankAccountCreate(DTO):
    """Bank account model to write to DB"""

    balance: NonNegativeInt = 0

    class Config:
        allow_mutation = False


class BankAccountRead(DTO):
    """Bank account output model from DB"""

    id: int
    balance: NonNegativeInt
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_mutation = False


class BankAccountUpdate(DTO):
    """Bank account update data model"""

    id: int
    amount: NonNegativeInt


class BankAccountSearch(DTO):
    """Bank account search data model"""

    id: Optional[int] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    customer_id: Optional[int] = None
