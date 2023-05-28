from datetime import date
from typing import Optional

from sqlalchemy import select, and_

from infrastructure.database.models.db import BankOperationModel
from ._base_repository import ProtocolRepo
from .sa_repository import SARepo


class OperationRepository(SARepo, ProtocolRepo):

    async def create(self, obj: BankOperationModel) -> BankOperationModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

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

    async def get_by_date_interval(self, start_date: date, end_date: date):
        query = (select(BankOperationModel)
                 .where(and_(BankOperationModel.created_at >= start_date,
                             BankOperationModel.created_at <= end_date)))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def update(self, obj: BankOperationModel):
        pass

    async def delete(self, obj_id: int):
        pass
