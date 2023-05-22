from .account import BankAccountCreate, BankAccountRead

from ._base import DTO


class CustomerInputDTO(DTO):
    """Bank customer input model"""
    first_name: str
    last_name: str


class BankCustomerCreate(DTO):
    """Bank customer model to write to DB"""
    first_name: str
    last_name: str
    bank_account: BankAccountCreate = BankAccountCreate(balance=0)


class BankCustomerRead(DTO):
    """Bank customer output model from DB"""
    id: int
    first_name: str
    last_name: str
    bank_account_id: int
    bank_account: BankAccountRead
