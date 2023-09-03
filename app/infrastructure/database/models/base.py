from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Integer, MetaData, sql, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry

convention = {
    "ix": "ix_%(column_0_label)s",                                          # INDEX
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",                          # UNIQUE
    "ck": "ck_%(table_name)s_%(constraint_name)s",                          # CHECK
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",  # FOREIGN KEY
    "pk": "pk_%(table_name)s",                                              # PRIMARY KEY
}

mapper_registry = registry(metadata=MetaData(naming_convention=convention))


class Base(DeclarativeBase):
    """Base DB model"""

    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True),
                                     # autoincrement=True
                                     default=uuid4,
                                     primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 nullable=False,
                                                 server_default=sql.func.now())


class UpdatedAtTimestampMixin:
    """Add 'updated_at' datetime column to DB model"""

    updated_at: Mapped[datetime] = mapped_column(DateTime,
                                                 nullable=False,
                                                 server_default=sql.func.now(),
                                                 onupdate=sql.func.now())
