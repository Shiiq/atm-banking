from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from common.settings import settings


db_engine = create_async_engine(url=settings.SQLITE_DATABASE_URL,
                                echo=False)

session_factory = async_sessionmaker(bind=db_engine,
                                     expire_on_commit=False)


# class Database:
#
#     def __init__(self, db_url: str):
#         self.__engine: AsyncEngine = create_async_engine(url=db_url,
#                                                          echo=True)
#         self.__session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self.__engine,
#                                                                                       expire_on_commit=False)
#
#     def get_session_factory(self):
#         return self.__session_factory
#
#     def get_engine(self):
#         return self.__engine
#
#
# async def create_engine(
#         db_url: str
# ) -> AsyncGenerator[AsyncEngine, None]:
#     engine = create_async_engine(url=db_url,
#                                  echo=True)
#     yield engine
#     await engine.dispose()
#
#
# def create_session_factory(
#         db_engine: AsyncEngine
# ) -> async_sessionmaker[AsyncSession]:
#     async_session_factory = async_sessionmaker(bind=db_engine,
#                                                expire_on_commit=False)
#     return async_session_factory
