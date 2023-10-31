from collections.abc import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker,
                                    create_async_engine)

from src.infrastructure.config.alter_db_config import DBConfig


async def create_engine(
        db_config: DBConfig,
        # metadata: MetaData
) -> AsyncGenerator[AsyncEngine, None]:

    if db_config.is_local:
        db_url = db_config.sqlite_url
    else:
        db_url = db_config.postgres_url
    engine = create_async_engine(
        url=db_url,
        echo=db_config.ECHO
    )
    print("create_engine")
    # async with engine.begin() as conn:
    #     await conn.run_sync(metadata.create_all)
    #     print("create_all")
    yield engine
    await engine.dispose()
    print("dispose_engine")


def create_session_factory(
        engine: AsyncEngine
) -> async_sessionmaker[AsyncSession]:

    async_session_factory = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )
    return async_session_factory


async def create_db_session(
        async_session_factory: async_sessionmaker[AsyncSession]
) -> AsyncGenerator[AsyncSession, None]:

    async with async_session_factory() as session:
        yield session


async def make_migrations(
        # engine: AsyncEngine,
        # metadata: MetaData
): # -> AsyncGenerator[None, None]:
    """For local startup only"""
    print("MAKE MIGRATIONDSSS")
    # print(metadata)
    # async with engine.begin() as conn:
    #     await conn.run_sync(metadata.drop_all)
    #     print("clear_database")
    #     await conn.run_sync(metadata.create_all)
    #     print("create_all")
    #     yield
    #     await conn.run_sync(metadata.drop_all)
    #     print("drop_database")
