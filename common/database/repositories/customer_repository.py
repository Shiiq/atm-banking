from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.database.models.db_models import BankCustomerModel
from common.database.repositories.abstract_repository import (
    AbstractRepository,
    ProtocolRepository,
    ConnHolder)


# class CustomerRepository(AbstractRepository[BankCustomerModel]):
class CustomerRepository(ConnHolder, ProtocolRepository):

    async def add(self, customer: BankCustomerModel):
        self._session.add(customer)
        await self._session.flush((customer,))
        return customer

    async def get_by_id(self, customer_id: int) -> Optional[BankCustomerModel]:
        query = (select(BankCustomerModel)
                 .where(BankCustomerModel.id == customer_id))
        customer = await self._session.execute(query)
        return customer.scalars().first()

    async def get_by_fullname(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        query = (select(BankCustomerModel)
                 .where(BankCustomerModel.first_name == first_name,
                        BankCustomerModel.last_name == last_name))
        customer = await self._session.execute(query)
        return customer.scalars().first()

    async def update(self, customer: BankCustomerModel):
        pass

    async def delete(self, customer_id: int):
        pass
