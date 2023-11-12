from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, UpdatedAtTimestampMixin

BANK_ACCOUNT = "bank_account"


class BankAccountModel(UpdatedAtTimestampMixin, Base):

    __tablename__ = BANK_ACCOUNT

    balance: Mapped[int] = mapped_column(Integer, default=0)
    customer = relationship(
        "BankCustomerModel",
        uselist=False,
        back_populates="bank_account"
    )
