from contextlib import asynccontextmanager, contextmanager
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker,
                                    create_async_engine)

from .db_config import DBConfig


# db_engine = create_async_engine(url=db_config.SQLITE_DATABASE_URL,
#                                 echo=False)
#
# session_factory = async_sessionmaker(bind=db_engine,
#                                      expire_on_commit=False)


@asynccontextmanager
async def create_engine(db_config: DBConfig) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(url=db_config.SQLITE_DATABASE_URL, echo=True)
    yield engine
    await engine.dispose()


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    async_session_factory = async_sessionmaker(bind=engine,
                                               autoflush=False,
                                               expire_on_commit=False)
    return async_session_factory
