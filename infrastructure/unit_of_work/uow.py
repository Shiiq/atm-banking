from sqlalchemy.ext.asyncio import AsyncSession


class UnitOfWork:
    _in_transaction: bool

    def __init__(
            self,
            session: AsyncSession,
    ):
        self._session = session
        print("hello from INIT uow")
        self._in_transaction = False

    async def __aenter__(self):
        if self._in_transaction:
            raise RuntimeError("Unit Of Work is already in transaction")

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
