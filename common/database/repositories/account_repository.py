from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.database.models.db_models import BankAccountModel
from common.database.repositories.abstract_repository import AbstractRepository


class AccountRepository(AbstractRepository[BankAccountModel]):

    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add(self, account: BankAccountModel):
        self.__session.add(account)
        await self.__session.flush((account,))
        return account

    async def get_by_id(self, account_id: int):
        stmt = (select(BankAccountModel)
                .where(BankAccountModel.id == account_id))
        account = await self.__session.execute(stmt)
        return account.scalars().first()

    async def update(self, account: BankAccountModel):
        pass

    async def delete(self, account_id: int):
        pass
