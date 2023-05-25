from typing import Optional

from .account import BankAccountCreate
from ._base import DTO


class CustomerInput(DTO):
    """Bank customer input model"""

    first_name: str
    last_name: str

    class Config:
        anystr_lower = True


class BankCustomerCreate(DTO):
    """Bank customer model to write to DB"""

    customer: CustomerInput
    bank_account: BankAccountCreate = BankAccountCreate(balance=0)

    class Config:
        allow_mutation = False


class BankCustomerRead(DTO):
    """Bank customer output model from DB"""

    id: int
    first_name: str
    last_name: str
    bank_account_id: int

    class Config:
        allow_mutation = False


class BankCustomerSearch(DTO):
    """Bank customer search data model"""

    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bank_account_id: Optional[int] = None
