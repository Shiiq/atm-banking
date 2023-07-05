from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.repositories import IAccountRepo, ICustomerRepo, IOperationRepo


class CustomValue:
    def __init__(self, value: str):
        print("INIT CustomValue")
        self.value = value

class UnitOfWork:
    _in_transaction: bool

    def __init__(
            self,
            session: AsyncSession,
            account_repo: IAccountRepo,
            customer_repo: ICustomerRepo,
            operation_repo: IOperationRepo,
            custom_value: CustomValue
    ):
        self._session = session
        print("hello from INIT uow")
        print("recieved CustomValue =>", custom_value, custom_value.value)
        self.cv = custom_value
        self._in_transaction = False
        # self.account_repo = account_repo(session)
        # self.customer_repo = customer_repo(session)
        # self.operation_repo = operation_repo(session)
        self.account_repo = account_repo
        self.customer_repo = customer_repo
        self.operation_repo = operation_repo

    def hello(self):
        print(50*"-", self.cv)

    async def __aenter__(self):
        if self._in_transaction:
            raise RuntimeError("Unit Of Work is already in transaction")

        await self._session.begin()
        self._in_transaction = True
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
            return
        else:
            await self.commit()
        self._in_transaction = False

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
