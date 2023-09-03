from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .account import BankAccountCreate
from .base import DTO, FrozenDTO


class BankCustomerCreate(FrozenDTO):
    """Bank customer model to write to DB"""

    first_name: str
    last_name: str
    bank_account: BankAccountCreate = Field(
        default_factory=BankAccountCreate
    )


class BankCustomerRead(FrozenDTO):
    """Bank customer output model from DB"""

    # id: int
    id: UUID
    first_name: str
    last_name: str
    # bank_account_id: int
    bank_account_id: UUID
    created_at: datetime
    updated_at: datetime


class BankCustomerSearch(DTO):
    """Bank customer search data model"""

    # id: Optional[int] = Field(default=None)
    id: Optional[UUID] = Field(default=None)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    # bank_account_id: Optional[int] = Field(default=None)
    bank_account_id: Optional[UUID] = Field(default=None)
