from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import mapped_column, relationship

from ._base import Base, UpdatedAtTimestampMixin


class BankCustomerModel(UpdatedAtTimestampMixin, Base):

    __tablename__ = "bank_customer"

    first_name = mapped_column(String(length=50), nullable=False)
    last_name = mapped_column(String(length=50), nullable=False)
    bank_account_id = mapped_column(Integer,
                                    ForeignKey("bank_account.id"),
                                    nullable=True)
    bank_account = relationship("BankAccountModel",
                                uselist=False,
                                back_populates="customer")

    __table_args__ = (
        UniqueConstraint("first_name", "last_name"),
        UniqueConstraint("id", "bank_account_id"),
    )
