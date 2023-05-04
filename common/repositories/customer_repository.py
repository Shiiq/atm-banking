from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.database.db_models import BankCustomerModel
from common.repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository[BankCustomerModel]):

    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add(self, customer: BankCustomerModel):
        self.__session.add(customer)
        await self.__session.commit()
        await self.__session.refresh(customer)
        return customer

    async def get_by_id(self, customer_id: int) -> Optional[BankCustomerModel]:
        stmt = (select(BankCustomerModel)
                .where(BankCustomerModel.id == customer_id))
        customer = await self.__session.execute(stmt)
        return customer.scalars().first()

    async def get_by_fullname(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        stmt = (select(BankCustomerModel)
                .where(BankCustomerModel.first_name == first_name,
                       BankCustomerModel.last_name == last_name))
        customer = await self.__session.execute(stmt)
        return customer.scalars().first()

    async def update(self, model: BankCustomerModel):
        pass

    async def delete(self, model_id: int):
        pass
