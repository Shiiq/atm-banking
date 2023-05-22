from pydantic import NonNegativeInt

from ._base import DTO


class BankAccountCreate(DTO):
    """Bank account model to write to DB"""
    balance: NonNegativeInt = 0


class BankAccountRead(DTO):
    """Bank account output model from DB"""
    id: int
    balance: NonNegativeInt


class BankAccountUpdate(DTO):
    """Bank account model to update"""
    id: int
    amount: NonNegativeInt
