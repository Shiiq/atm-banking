from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.repositories import ProtocolRepo


class UnitOfWork:

    def __init__(
            self,
            session: AsyncSession,
            account_repo: Type[ProtocolRepo],
            customer_repo: Type[ProtocolRepo],
            operation_repo: Type[ProtocolRepo]
    ):
        self._session = session
        self.account_repo = account_repo(session)
        self.customer_repo = customer_repo(session)
        self.operation_repo = operation_repo(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
            return
        else:
            await self.commit()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
