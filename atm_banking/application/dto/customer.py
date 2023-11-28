from datetime import datetime
from uuid import UUID

from pydantic import Field

from .account import BankAccountCreate, BankAccountRead
from .base import FrozenDTO


class BankCustomerCreate(FrozenDTO):
    """Bank customer data model for creating."""

    first_name: str
    last_name: str
    bank_account: BankAccountCreate = Field(
        default_factory=BankAccountCreate
    )


class BankCustomerRead(FrozenDTO):
    """Bank customer output data model from DB."""

    id: UUID
    first_name: str
    last_name: str
    bank_account_id: UUID
    created_at: datetime
    updated_at: datetime
    bank_account: BankAccountRead
