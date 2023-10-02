from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .account import BankAccountCreate, BankAccountRead
from .base import DTO, FrozenDTO


class BankCustomerCreate(FrozenDTO):
    """Bank customer model for creating"""

    first_name: str
    last_name: str
    bank_account: BankAccountCreate = Field(
        default_factory=BankAccountCreate
    )


class BankCustomerRead(FrozenDTO):
    """Bank customer output model from DB"""

    id: UUID
    first_name: str
    last_name: str
    bank_account_id: UUID
    created_at: datetime
    updated_at: datetime
    bank_account: Optional[BankAccountRead] = Field(default=None)


class BankCustomerSearch(DTO):
    """Bank customer search data model"""

    id: Optional[UUID] = Field(default=None)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    bank_account_id: Optional[UUID] = Field(default=None)
