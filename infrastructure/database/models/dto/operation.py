from datetime import date, datetime, time
from typing import Optional

from pydantic import PositiveInt, validator, ValidationError

from infrastructure.database.models.constants import BankOperationsToDB
from ._base import DTO, FrozenDTO


class BankOperationCreate(FrozenDTO):
    """Bank operation model to write to DB"""

    amount: PositiveInt
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationsToDB


class BankOperationRead(FrozenDTO):
    """Bank operation output model from DB"""

    id: int
    amount: PositiveInt
    bank_account_id: int
    bank_customer_id: int
    bank_operation_type: BankOperationsToDB
    created_at: datetime


class BankOperationSearch(DTO):
    """Bank operation search data model"""

    id: Optional[int] = None
    bank_account_id: Optional[int] = None
    bank_customer_id: Optional[int] = None
    bank_operation_type: Optional[BankOperationsToDB] = None
    since: Optional[datetime] = None
    till: Optional[datetime] = None

    @validator("since", pre=True)
    def convert_since_to_datetime(cls, d: date) -> datetime:
        t = time(hour=0, minute=0, second=0, microsecond=0)
        return datetime.combine(d, t)

    @validator("till", pre=True)
    def convert_till_to_datetime(cls, d: date) -> datetime:
        t = time(hour=23, minute=59, second=59, microsecond=999999)
        return datetime.combine(d, t)
