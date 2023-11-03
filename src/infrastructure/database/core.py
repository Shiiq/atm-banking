from collections.abc import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from src.infrastructure.config.db_config import DBConfig


async def create_engine(
        db_config: DBConfig
) -> AsyncGenerator[AsyncEngine, None]:

    # if db_config.is_local:
    #     db_url = db_config.sqlite_url
    # else:
    #     db_url = db_config.postgres_url

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
        print(10*"-", id(conn))
        await conn.run_sync(metadata.drop_all)
        print("clear_database")

        await conn.run_sync(metadata.create_all)
        print("create_database")

        yield engine

        await conn.run_sync(metadata.drop_all)
        print("drop_database")

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
