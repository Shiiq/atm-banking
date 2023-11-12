from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import NonNegativeInt

from .base import DTO, FrozenDTO

DEFAULT_BALANCE = 0


class BankAccountCreate(FrozenDTO):
    """Bank account data model for creating."""

    balance: NonNegativeInt = DEFAULT_BALANCE


class BankAccountRead(FrozenDTO):
    """Bank account output data model from DB."""

    id: UUID
    balance: NonNegativeInt
    created_at: datetime
    updated_at: datetime


class BankAccountUpdate(DTO):
    """Bank account update data model."""

    id: UUID
    balance: NonNegativeInt
