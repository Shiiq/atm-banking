from sqlalchemy import Enum, ForeignKey, Integer
from sqlalchemy.orm import mapped_column

from infrastructure.database.models.constants import BankOperationsToDB
from ._base import Base


class BankOperationModel(Base):

    __tablename__ = "bank_operation"

    amount = mapped_column(Integer, nullable=False)
    bank_account_id = mapped_column(Integer,
                                    ForeignKey("bank_account.id"),
                                    nullable=False)
    bank_customer_id = mapped_column(Integer,
                                     ForeignKey("bank_customer.id"),
                                     nullable=False)
    bank_operation = mapped_column(Enum(BankOperationsToDB),
                                   nullable=False)
