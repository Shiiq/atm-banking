from datetime import date, datetime
from typing import Optional

from pydantic import PositiveInt

from common.database.models.constants import BankOperationsToDB, BankOperationsFromInput
from ._base import DTO


class OperationInput(DTO):
    """Bank operation input model"""

    type_: BankOperationsFromInput
    amount: Optional[PositiveInt] = None
    since: Optional[date] = None
    till: Optional[date] = None


class BankOperationCreate(DTO):
    """Bank operation model to write to DB"""

    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation: BankOperationsToDB

    class Config:
        allow_mutation = False


class BankOperationRead(DTO):
    """Bank operation output model from DB"""

    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation: BankOperationsToDB
    created_at: datetime

    class Config:
        allow_mutation = False
