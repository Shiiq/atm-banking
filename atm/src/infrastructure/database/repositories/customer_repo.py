from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.application.interfaces import ICustomerRepo
from src.infrastructure.database.models import BankCustomerModel


class CustomerRepo(ICustomerRepo):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(
            self,
            customer: BankCustomerModel
    ) -> BankCustomerModel:

        self._session.add(customer)
        await self._session.flush()
        return customer

    async def get_by_id(
            self,
            customer_id: UUID
    ) -> Optional[BankCustomerModel]:

        customer = await self._session.get(
            BankCustomerModel,
            customer_id,
            options=[joinedload(BankCustomerModel.bank_account), ]
        )
        return customer

    async def get_by_fullname(
            self,
            customer_first_name: str,
            customer_last_name: str
    ) -> Optional[BankCustomerModel]:

        query = (
            select(BankCustomerModel)
            .where(BankCustomerModel.first_name == customer_first_name,
                   BankCustomerModel.last_name == customer_last_name)
            .options(joinedload(BankCustomerModel.bank_account))
        )
        customer = await self._session.scalar(query)
        return customer
