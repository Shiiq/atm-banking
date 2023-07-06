from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from infrastructure.database.models.db import BankCustomerModel
from .sa_repository import SARepo
from .interfaces import ICustomerRepo


class CustomerRepo(SARepo, ICustomerRepo):

    def __init__(self, session: AsyncSession):
        print("hello from INIT CusRepo")
        super().__init__(session)

    async def create(self, obj: BankCustomerModel) -> BankCustomerModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_by_id(self, obj_id: int) -> Optional[BankCustomerModel]:
        obj = await self._session.get(
            BankCustomerModel,
            obj_id,
            options=[joinedload(BankCustomerModel.bank_account), ])
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
        return obj

    async def update(self, obj: BankCustomerModel):
        await self._session.merge(obj)
        return obj
