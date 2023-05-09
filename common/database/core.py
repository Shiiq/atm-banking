from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker,
                                    create_async_engine)

from common.settings import settings


db_engine = create_async_engine(url=settings.SQLITE_DATABASE_URL,
                                echo=False)

session_factory = async_sessionmaker(bind=db_engine,
                                     expire_on_commit=False)

async def create_engine(db_url: str) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(url=db_url,
                                 echo=True)
    yield engine
    await engine.dispose()


def create_session_factory(db_engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    async_session_factory = async_sessionmaker(bind=db_engine,
                                               expire_on_commit=False)
    return async_session_factory
