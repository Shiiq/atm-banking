from sqlalchemy import Enum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.constants import BankOperationsToDB
from .base import Base

BANK_OPERATION = "bank_operation"


class BankOperationModel(Base):

    __tablename__ = BANK_OPERATION

    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    bank_account_id: Mapped[int] = mapped_column(Integer,
                                                 ForeignKey("bank_account.id"),
                                                 nullable=False)
    bank_customer_id: Mapped[int] = mapped_column(Integer,
                                                  ForeignKey("bank_customer.id"),
                                                  nullable=False)
    bank_operation_type = mapped_column(Enum(BankOperationsToDB),
                                        nullable=False)
