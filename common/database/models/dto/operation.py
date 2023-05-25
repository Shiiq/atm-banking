from datetime import date, datetime
from typing import Optional

from pydantic import PositiveInt

from common.database.models.constants import BankOperationsToDB, BankOperationsFromInput
from ._base import DTO


class OperationInput(DTO):
    type_: BankOperationsFromInput
    amount: Optional[int] = PositiveInt
    since: Optional[date] = None
    till: Optional[date] = None


class BankOperationCreate(DTO):
    """Bank operation model to write to DB"""
    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation: BankOperationsToDB


class BankOperationRead(DTO):
    """Bank operation output model from DB"""
    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation: BankOperationsToDB
    created_at: datetime
