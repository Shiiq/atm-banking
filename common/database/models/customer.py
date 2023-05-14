from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import mapped_column, relationship

from .base import Base, UpdatedAtTimestamp


class BankCustomerModel(UpdatedAtTimestamp, Base):
    __tablename__ = "bank_customer"

    first_name = mapped_column(String(length=50), nullable=False)
    last_name = mapped_column(String(length=50), nullable=False)
    bank_account = relationship("BankAccountModel",
                                uselist=False,
                                back_populates="customer")
    bank_account_id = mapped_column(Integer,
                                    ForeignKey("bank_account.id"),
                                    nullable=True)

    __table_args__ = (
        UniqueConstraint("first_name", "last_name"),
        UniqueConstraint("id", "bank_account_id"),
    )
