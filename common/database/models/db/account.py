from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, relationship

from .base import Base, UpdatedAtTimestampMixin


class BankAccountModel(UpdatedAtTimestampMixin, Base):
    __tablename__ = "bank_account"

    balance = mapped_column(Integer, default=0)

    customer = relationship("BankCustomerModel",
                            uselist=False,
                            back_populates="bank_account")
