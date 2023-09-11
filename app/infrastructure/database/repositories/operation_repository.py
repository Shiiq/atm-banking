from datetime import datetime
from typing import Optional

from sqlalchemy import select, inspect
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models import BankOperationModel
from .interfaces import IOperationRepo
from .sa_repository import SARepo


class OperationRepo(SARepo, IOperationRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(
            self,
            operation: BankOperationModel
    ) -> BankOperationModel:
        # print(50*"-")
        # print("OPERATION REPO CREATE METH BEFORE ADD TO SESS")
        # for i in self._session.identity_map.values():
        #     print(i)
        #     print("TRANSIENT", inspect(i).transient)
        #     print("PENDING", inspect(i).pending)
        #     print("PERSISTENT", inspect(i).persistent)
        #     print("DELETED", inspect(i).deleted)
        #     print("DETACHED", inspect(i).detached)
        # print("TRANSIENT", inspect(operation).transient)
        # print("PENDING", inspect(operation).pending)
        # print("PERSISTENT", inspect(operation).persistent)
        # print("DELETED", inspect(operation).deleted)
        # print("DETACHED", inspect(operation).detached)
        self._session.add(operation)
        # print("OPERATION REPO CREATE METH AFTER ADD TO SESS BEFORE FLUSH")
        # for i in self._session.identity_map.values():
        #     print(i)
        # print("TRANSIENT", inspect(operation).transient)
        # print("PENDING", inspect(operation).pending)
        # print("PERSISTENT", inspect(operation).persistent)
        # print("DELETED", inspect(operation).deleted)
        # print("DETACHED", inspect(operation).detached)
            # print("TRANSIENT", inspect(i).transient)
            # print("PENDING", inspect(i).pending)
            # print("PERSISTENT", inspect(i).persistent)
            # print("DELETED", inspect(i).deleted)
            # print("DETACHED", inspect(i).detached)
        await self._session.flush()
        # print("OPERATION REPO CREATE METH AFTER FLUSH")
        # print("TRANSIENT", inspect(operation).transient)
        # print("PENDING", inspect(operation).pending)
        # print("PERSISTENT", inspect(operation).persistent)
        # print("DELETED", inspect(operation).deleted)
        # print("DETACHED", inspect(operation).detached)
        # for i in self._session.identity_map.values():
        #     print(i)
        #     print("TRANSIENT", inspect(i).transient)
        #     print("PENDING", inspect(i).pending)
        #     print("PERSISTENT", inspect(i).persistent)
        #     print("DELETED", inspect(i).deleted)
        #     print("DETACHED", inspect(i).detached)
        # print(50*"-")
        return operation

    async def get_all(self):

        query = (select(BankOperationModel))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_id(
            self,
            operation_id: int
    ) -> Optional[BankOperationModel]:

        query = (select(BankOperationModel)
                 .where(BankOperationModel.id == operation_id))
        operation = await self._session.execute(query)
        return operation.scalars().first()

    async def get_by_account_id(
            self,
            account_id: int
    ):

        query = (select(BankOperationModel)
                 .where(BankOperationModel.bank_account_id == account_id))
        operations = await self._session.execute(query)
        return operations.scalars().all()

    async def get_by_customer_id(
            self,
            customer_id: int
    ):

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
