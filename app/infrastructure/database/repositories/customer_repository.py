from typing import Optional

from sqlalchemy import select, inspect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.infrastructure.database.models import BankCustomerModel
from .interfaces import ICustomerRepo
from .sa_repository import SARepo


class CustomerRepo(SARepo, ICustomerRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(
            self,
            customer: BankCustomerModel
    ) -> BankCustomerModel:

        self._session.add(customer)
        await self._session.flush()
        return customer

    async def get_by_id(
            self,
            customer_id: int
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

        query = (select(BankCustomerModel)
                 .where(BankCustomerModel.first_name == customer_first_name,
                        BankCustomerModel.last_name == customer_last_name)
                 .options(joinedload(BankCustomerModel.bank_account)))
        customer = await self._session.scalar(query)
        # print(50*"-")
        # print("CUSTOMER REPO GET BY FULLNAME METH")
        # for i in self._session.identity_map.values():
        #     print(i)
        #     print("TRANSIENT", inspect(i).transient)
        #     print("PENDING", inspect(i).pending)
        #     print("PERSISTENT", inspect(i).persistent)
        #     print("DELETED", inspect(i).deleted)
        #     print("DETACHED", inspect(i).detached)
        # print(50*"-")
        return customer
