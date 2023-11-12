from uuid import UUID

from sqlalchemy import ForeignKey, String, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, UpdatedAtTimestampMixin

BANK_CUSTOMER = "bank_customer"


class BankCustomerModel(UpdatedAtTimestampMixin, Base):

    __tablename__ = BANK_CUSTOMER

    first_name: Mapped[str] = mapped_column(
        String(length=50),
        nullable=False
    )
    last_name: Mapped[str] = mapped_column(
        String(length=50),
        nullable=False
    )
    bank_account_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("bank_account.id"),
        nullable=True
    )
    bank_account = relationship(
        "BankAccountModel",
        uselist=False,
        back_populates="customer"
    )

    __table_args__ = (
        UniqueConstraint("first_name", "last_name"),
        UniqueConstraint("id", "bank_account_id"),
    )
