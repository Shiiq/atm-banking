from datetime import datetime
from typing import Optional

from sqlalchemy import select

from infrastructure.database.models.db import BankOperationModel
from .sa_repository import SARepo
from ._base_repository import ProtocolRepo


class OperationRepository(SARepo, ProtocolRepo):

    async def create(self, obj: BankOperationModel) -> BankOperationModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_all(self):
        query = (select(BankOperationModel))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_id(self, obj_id: int) -> Optional[BankOperationModel]:
        query = (select(BankOperationModel)
                 .where(BankOperationModel.id == obj_id))
        operation = await self._session.execute(query)
        return operation.scalars().first()

    async def get_by_customer_id(self, customer_id: int):
        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_customer_id == customer_id))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_bank_account_id(self, bank_account_id: int):
        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_account_id == bank_account_id))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_date_interval(
            self,
            customer_id: int,
            bank_account_id: int,
            start_date: datetime,
            end_date: datetime
    ):
        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_customer_id == customer_id,
                        BankOperationModel.bank_account_id == bank_account_id)
                 .where(BankOperationModel.created_at.between(start_date,
                                                              end_date)))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def update(self, obj: BankOperationModel):
        pass

    async def delete(self, obj_id: int):
        pass
