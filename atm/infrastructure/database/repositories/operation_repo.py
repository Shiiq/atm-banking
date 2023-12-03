from datetime import datetime
from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from atm.application.interfaces import IOperationRepo
from atm.infrastructure.database.models import BankOperationModel


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

    async def get_by_date_interval(
            self,
            account_id: UUID,
            customer_id: UUID,
            start_date: datetime,
            end_date: datetime
    ) -> Sequence[BankOperationModel]:

        query = (
            select(BankOperationModel)
            .where(BankOperationModel.bank_account_id == account_id,
                   BankOperationModel.bank_customer_id == customer_id)
            .where(BankOperationModel.created_at.between(start_date,
                                                         end_date))
        )
        operations = await self._session.execute(query)
        return operations.scalars().all()
