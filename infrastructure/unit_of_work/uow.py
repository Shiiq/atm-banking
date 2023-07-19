from sqlalchemy.ext.asyncio import AsyncSession


class UnitOfWorkError(Exception):

    @property
    def message(self):
        return "Unit Of Work is already in transaction"

    def __str__(self):
        return self.message


class UnitOfWork:
    _in_transaction: bool

    def __init__(
            self,
            session: AsyncSession,
    ):
        self._session = session
        self._in_transaction = False

    async def __aenter__(self):
        if self._in_transaction:
            raise UnitOfWorkError()

        self._in_transaction = True
        await self._session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self._rollback()
        else:
            await self._commit()
        self._in_transaction = False

    async def _commit(self):
        await self._session.commit()

    async def _rollback(self):
        await self._session.rollback()
