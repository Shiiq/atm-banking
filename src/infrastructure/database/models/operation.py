from enum import StrEnum
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

BANK_OPERATION = "bank_operation"


class BankOperationsDB(StrEnum):
    """Bank operations to write to DB"""

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class BankOperationModel(Base):

    __tablename__ = BANK_OPERATION

    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    bank_account_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("bank_account.id"),
        nullable=False
    )
    bank_customer_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("bank_customer.id"),
        nullable=False
    )
    bank_operation_type: Mapped[str] = mapped_column(
        Enum(BankOperationsDB),
        nullable=False
    )
