from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, relationship

from .base import BaseModel, UpdatedAtTimestamp


class BankAccountModel(UpdatedAtTimestamp, BaseModel):
    __tablename__ = "bank_account"

    deposit = mapped_column(Integer, default=0)
    holder = relationship("BankCustomerModel",
                          uselist=False,
                          back_populates="bank_account")
