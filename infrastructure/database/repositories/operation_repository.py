from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.models.db import BankOperationModel
from .sa_repository import SARepo
from .interfaces import IOperationRepo


class OperationRepo(SARepo, IOperationRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, operation: BankOperationModel) -> BankOperationModel:
        self._session.add(operation)
        await self._session.flush()
        return operation

    async def get_all(self):
        query = (select(BankOperationModel))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_id(self, operation_id: int) -> Optional[BankOperationModel]:
        query = (select(BankOperationModel)
                 .where(BankOperationModel.id == operation_id))
        operation = await self._session.execute(query)
        return operation.scalars().first()

    async def get_by_account_id(self, account_id: int):
        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_account_id == account_id))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_customer_id(self, customer_id: int):
        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_customer_id == customer_id))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_date_interval(
            self,
            account_id: int,
            customer_id: int,
            start_date: datetime,
            end_date: datetime
    ):
        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_account_id == account_id,
                        BankOperationModel.bank_customer_id == customer_id,)
                 .where(BankOperationModel.created_at.between(start_date,
                                                              end_date)))
        operations = await self._session.execute(query)
        return operations.scalars().all()
