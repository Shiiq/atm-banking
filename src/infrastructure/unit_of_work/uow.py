from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces import IUnitOfWork


class UnitOfWorkError(Exception):

    @property
    def msg(self):
        return "Unit Of Work is already in transaction"

    def __str__(self):
        return self.msg


class UnitOfWork(IUnitOfWork):

    _in_transaction: bool

    def __init__(self, session: AsyncSession):
        self._session = session
        self._in_transaction = False

    async def __aenter__(self):
        if self._in_transaction:
            raise UnitOfWorkError()

        self._in_transaction = True
        await self._session.begin()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        self._in_transaction = False

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
