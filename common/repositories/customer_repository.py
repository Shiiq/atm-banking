from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.database.db_models import BankCustomerModel
from common.repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository[BankCustomerModel]):

    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__model = BankCustomerModel

    async def add(self, model: BankCustomerModel):
        pass

    async def get_by_id(self, model_id: int) -> Optional[BankCustomerModel]:
        stmt = (select(BankCustomerModel)
                .where(BankCustomerModel.id == model_id))
        customer = await self.__session.execute(stmt)
        return customer.scalars().first()

    async def update(self, model: BankCustomerModel):
        pass

    async def delete(self, model_id: int):
        pass
