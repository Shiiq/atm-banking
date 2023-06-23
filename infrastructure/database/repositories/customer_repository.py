from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.database.models.db import BankCustomerModel
from application.exceptions import CustomerNotExist, CustomerIDNotExist
from .sa_repository import SARepo
from ._base_repository import ProtocolRepo


class CustomerRepository(SARepo, ProtocolRepo):

    async def create(self, obj: BankCustomerModel) -> BankCustomerModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_by_id(self, obj_id: int) -> Optional[BankCustomerModel]:
        obj = await self._session.get(
            BankCustomerModel,
            obj_id,
            options=[joinedload(BankCustomerModel.bank_account), ])
        if not obj:
            raise CustomerIDNotExist(obj_id=obj_id)
        return obj
    #     query = (select(BankCustomerModel)
    #              .where(BankCustomerModel.id == obj_id)
    #              .options(joinedload(BankCustomerModel.bank_account)))
    #     customer = await self._session.execute(query)
    #     return customer.scalars().first()

    # async def get_by_account_id(self, obj_id: int) -> BankCustomerModel:
    #     query = (select(BankCustomerModel)
    #              .where(BankCustomerModel.bank_account_id == obj_id)
    #              .options(joinedload(BankCustomerModel.bank_account)))
    #     customer = await self._session.execute(query)
    #     return customer.scalars().first()

    async def get_by_fullname(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        query = (select(BankCustomerModel)
                 .where(BankCustomerModel.first_name == first_name,
                        BankCustomerModel.last_name == last_name)
                 .options(joinedload(BankCustomerModel.bank_account)))
        obj = await self._session.scalar(query)
        if not obj:
            raise CustomerNotExist(first_name=first_name, last_name=last_name)
        return obj
        # return customer.scalars().first()

    async def update(self, obj: BankCustomerModel):
        await self._session.merge(obj)
        return obj
