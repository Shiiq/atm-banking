from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.database.db_models import BankCustomerModel, BankAccountModel
from common.repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository[BankAccountModel]):

    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add(self, account: BankAccountModel):
        self.__session.add(account)
        await self.__session.commit()
        await self.__session.refresh(account)
        return account

    async def get_by_id(self, account_id: int):
        pass

    async def update(self, model: BankAccountModel):
        pass

    async def delete(self, model_id: int):
        pass
