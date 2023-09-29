from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models import BankOperationModel
from .interfaces import IOperationRepo


class OperationRepo(IOperationRepo):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(
            self,
            operation: BankOperationModel
    ) -> BankOperationModel:

        self._session.add(operation)
        await self._session.flush()
        return operation

    async def get_all(self):

        query = (select(BankOperationModel))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_id(
            self,
            operation_id: UUID
    ) -> Optional[BankOperationModel]:

        query = (select(BankOperationModel)
                 .where(BankOperationModel.id == operation_id))
        operation = await self._session.execute(query)
        return operation.scalars().first()

    async def get_by_customer_id(
            self,
            account_id: UUID,
            customer_id: UUID,
    ):

        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_account_id == account_id,
                        BankOperationModel.bank_customer_id == customer_id))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_date_interval(
            self,
            account_id: UUID,
            customer_id: UUID,
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
