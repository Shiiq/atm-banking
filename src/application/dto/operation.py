from datetime import datetime
from uuid import UUID

from pydantic import PositiveInt

from .base import BankOperationType, FrozenDTO


class BankOperationCreate(FrozenDTO):
    """Bank operation data model for creating."""

    amount: PositiveInt
    bank_account_id: UUID
    bank_customer_id: UUID
    bank_operation_type: BankOperationType


class BankOperationRead(FrozenDTO):
    """Bank operation output data model from DB."""

    id: UUID
    amount: PositiveInt
    bank_account_id: UUID
    bank_customer_id: UUID
    bank_operation_type: BankOperationType
    created_at: datetime
