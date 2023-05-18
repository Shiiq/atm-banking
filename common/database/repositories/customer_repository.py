from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from common.database.models import BankCustomerModel
from common.database.repositories.abstract_repository import ProtocolRepository, ConnHolder


class CustomerRepository(ConnHolder, ProtocolRepository):

    async def create(self, obj: BankCustomerModel) -> BankCustomerModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_by_id(self, obj_id: int) -> Optional[BankCustomerModel]:
        query = (select(BankCustomerModel)
                 .where(BankCustomerModel.id == obj_id)
                 .options(joinedload(BankCustomerModel.bank_account)))
        customer = await self._session.execute(query)
        return customer.scalars().first()

    async def get_by_fullname(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        query = (select(BankCustomerModel)
                 .where(BankCustomerModel.first_name == first_name,
                        BankCustomerModel.last_name == last_name)
                 .options(joinedload(BankCustomerModel.bank_account)))
        customer = await self._session.execute(query)
        return customer.scalars().first()

    async def update(self, obj: BankCustomerModel):
        pass

    async def delete(self, obj_id: int):
        pass
