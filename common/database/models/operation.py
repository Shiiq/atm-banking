from enum import StrEnum

from sqlalchemy import Enum, ForeignKey, Integer
from sqlalchemy.orm import mapped_column

from .base import BaseModel


class BankOperationsToDB(StrEnum):
    """Bank operations to write to database"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class BankOperationModel(BaseModel):
    __tablename__ = "bank_operation"

    bank_customer = mapped_column(Integer,
                                  ForeignKey("bank_customer.id"),
                                  nullable=False)
    bank_account = mapped_column(Integer,
                                 ForeignKey("bank_account.id"),
                                 nullable=False)
    bank_operation = mapped_column(Enum(BankOperationsToDB),
                                   nullable=False)
    amount = mapped_column(Integer, nullable=False)
