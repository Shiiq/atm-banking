from sqlalchemy import DateTime, Integer, MetaData, sql
from sqlalchemy.orm import DeclarativeBase, mapped_column, registry

convention = {
    "ix": "ix_%(column_0_label)s",  # INDEX
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",  # UNIQUE
    "ck": "ck_%(table_name)s_%(constraint_name)s",  # CHECK
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",  # FOREIGN KEY
    "pk": "pk_%(table_name)s",  # PRIMARY KEY
}

mapper_registry = registry(metadata=MetaData(naming_convention=convention))


class UpdatedAtTimestamp:
    """Add 'updated_at' datetime column to DB model"""

    updated_at = mapped_column(DateTime,
                               nullable=False,
                               server_default=sql.func.now(),
                               onupdate=sql.func.now())


class BaseModel(DeclarativeBase):
    """Base model"""

    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at = mapped_column(DateTime,
                               nullable=False,
                               server_default=sql.func.now())
