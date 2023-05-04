from sqlalchemy.ext.asyncio import AsyncSession

from common.database.models.db_models import BankAccountModel, BankCustomerModel
from common.database.repositories.abstract_repository import AbstractRepository


class UnitOfWork:

    def __init__(
            self,
            session: AsyncSession,
            account_rep: AbstractRepository[BankAccountModel],
            customer_rep: AbstractRepository[BankCustomerModel]
    ):
        self.session = session
        self.account_rep = account_rep
        self.customer_rep = customer_rep

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
