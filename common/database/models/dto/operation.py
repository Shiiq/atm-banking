from datetime import datetime

from common.database.models.constants import BankOperationsToDB
from ._base import DTO


class BankOperationCreate(DTO):
    """Bank operation output model from DB"""
    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation: BankOperationsToDB


class BankOperationRead(DTO):
    """Bank operation model to write to DB"""
    amount: int
    bank_account_id: int
    bank_customer_id: int
    bank_operation: BankOperationsToDB
    created_at: datetime
