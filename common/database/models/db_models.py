# from sqlalchemy import DateTime, Enum, ForeignKey, Integer, MetaData, String, UniqueConstraint, sql
# from sqlalchemy.orm import DeclarativeBase, mapped_column, registry, relationship
#
#
# convention = {
#     "ix": "ix_%(column_0_label)s",  # INDEX
#     "uq": "uq_%(table_name)s_%(column_0_N_name)s",  # UNIQUE
#     "ck": "ck_%(table_name)s_%(constraint_name)s",  # CHECK
#     "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",  # FOREIGN KEY
#     "pk": "pk_%(table_name)s",  # PRIMARY KEY
# }
#
# mapper_registry = registry(metadata=MetaData(naming_convention=convention))
#
#
# class UpdatedAtTimestamp:
#     """Add 'updated_at' datetime column to DB model"""
#
#     updated_at = mapped_column(DateTime,
#                                nullable=False,
#                                server_default=sql.func.now(),
#                                onupdate=sql.func.now())
#
#
# class BaseModel(DeclarativeBase):
#     """Base model"""
#
#     __abstract__ = True
#
#     registry = mapper_registry
#     metadata = mapper_registry.metadata
#     id = mapped_column(Integer, primary_key=True, autoincrement=True)
#     created_at = mapped_column(DateTime,
#                                nullable=False,
#                                server_default=sql.func.now())
#
#
# class BankCustomerModel(UpdatedAtTimestamp, BaseModel):
#     __tablename__ = "bank_customer"
#
#     first_name = mapped_column(String(length=50), nullable=False)
#     last_name = mapped_column(String(length=50), nullable=False)
#     bank_account = relationship("BankAccountModel",
#                                 uselist=False,
#                                 back_populates="holder")
#     bank_account_id = mapped_column(Integer,
#                                     ForeignKey("bank_account.id"),
#                                     nullable=True)
#
#     __table_args__ = (
#         UniqueConstraint("first_name", "last_name"),
#         UniqueConstraint("id", "bank_account_id"),
#     )
#
#
# class BankAccountModel(UpdatedAtTimestamp, BaseModel):
#     __tablename__ = "bank_account"
#
#     deposit = mapped_column(Integer, default=0)
#     holder = relationship("BankCustomerModel",
#                           uselist=False,
#                           back_populates="bank_account")
#
#
# class BankOperationModel(BaseModel):
#     __tablename__ = "bank_operation"
#
#     bank_client = mapped_column(Integer,
#                                 ForeignKey("bank_customer.id"),
#                                 nullable=False)
#     bank_account = mapped_column(Integer,
#                                  ForeignKey("bank_account.id"),
#                                  nullable=False)
#     bank_operation = mapped_column(Enum(BankOperationsToDB),
#                                    nullable=False)
#     amount = mapped_column(Integer, nullable=False)
