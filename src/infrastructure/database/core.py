from collections.abc import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from .db_config import DBConfig


async def create_engine_remote_way(
        db_config: DBConfig
) -> AsyncGenerator[AsyncEngine, None]:

    engine = create_async_engine(
        url=db_config.postgres_url,
        echo=db_config.echo
    )
    yield engine
    await engine.dispose()


async def create_engine_local_way(
        db_config: DBConfig,
        metadata: MetaData
) -> AsyncGenerator[AsyncEngine, None]:

    engine = create_async_engine(
        url=db_config.sqlite_url,
        echo=db_config.echo
    )
    async with engine.connect() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
        yield engine
        await conn.run_sync(metadata.drop_all)
    await engine.dispose()


def create_session_factory(
        engine: AsyncEngine
) -> async_sessionmaker:

    async_session_factory = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )
    return async_session_factory


async def create_db_session(
        async_session_factory: async_sessionmaker
) -> AsyncGenerator[AsyncSession, None]:

    async with async_session_factory() as session:
        yield session
