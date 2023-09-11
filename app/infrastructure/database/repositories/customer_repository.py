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
        print(50*"-")
        print("TRANSIENT", inspect(customer).transient)
        print("PENDING", inspect(customer).pending)
        print("PERSISTENT", inspect(customer).persistent)
        print("DELETED", inspect(customer).deleted)
        print("DETACHED", inspect(customer).detached)
        print("TRANSIENT", inspect(customer.bank_account).transient)
        print("PENDING", inspect(customer.bank_account).pending)
        print("PERSISTENT", inspect(customer.bank_account).persistent)
        print("DELETED", inspect(customer.bank_account).deleted)
        print("DETACHED", inspect(customer.bank_account).detached)
        for i in self._session.identity_map.values():
            print(i)
        print(50*"-")
        return customer
