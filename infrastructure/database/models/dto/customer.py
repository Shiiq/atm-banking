from datetime import datetime
from typing import Optional

from .account import BankAccountCreate
from ._base import DTO, FrozenDTO


class BankCustomerCreate(FrozenDTO):
    """Bank customer model to write to DB"""

    first_name: str
    last_name: str
    bank_account: BankAccountCreate = BankAccountCreate(balance=0)


class BankCustomerRead(FrozenDTO):
    """Bank customer output model from DB"""

    id: int
    first_name: str
    last_name: str
    bank_account_id: int
    created_at: datetime
    updated_at: datetime


class BankCustomerSearch(DTO):
    """Bank customer search data model"""

    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bank_account_id: Optional[int] = None
