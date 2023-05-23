from datetime import datetime

from pydantic import NonNegativeInt

from ._base import DTO


class BankAccountCreate(DTO):
    """Bank account model to write to DB"""
    balance: NonNegativeInt


class BankAccountRead(DTO):
    """Bank account output model from DB"""
    id: int
    balance: NonNegativeInt
    created_at: datetime
    updated_at: datetime


class BankAccountUpdate(DTO):
    """Bank account model to update"""
    id: int
    balance: NonNegativeInt
