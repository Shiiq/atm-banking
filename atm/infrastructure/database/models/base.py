from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, MetaData, sql, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry

convention = {
    # index
    "ix": "ix_%(column_0_label)s",
    # unique
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    # check
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    # foreign key
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    # primary key
    "pk": "pk_%(table_name)s"
}

mapper_registry = registry(metadata=MetaData(naming_convention=convention))


class Base(DeclarativeBase):
    """Base DB model."""

    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        default=uuid4,
        primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=sql.func.now()
    )


class UpdatedAtTimestampMixin:
    """'updated_at' datetime column mixin."""

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        onupdate=sql.func.now(),
        server_default=sql.func.now()
    )
