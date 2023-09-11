from typing import Optional

from sqlalchemy import select, inspect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.infrastructure.database.models import BankAccountModel
from .interfaces import IAccountRepo
from .sa_repository import SARepo


class AccountRepo(SARepo, IAccountRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(
            self,
            account: BankAccountModel
    ) -> BankAccountModel:

        self._session.add(account)
        await self._session.flush()
        return account

    async def get_by_id(
            self,
            account_id: int
    ) -> Optional[BankAccountModel]:

        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == account_id)
                 .with_for_update())
        account = await self._session.execute(query)
        return account.scalars().first()

    # async def update(
    #         self,
    #         account: BankAccountModel
    # ) -> BankAccountModel:
    #
    #     await self._session.flush()
    #     await self._session.refresh(account)
    #     return account

    async def update(
            self,
            account: BankAccountModel
    ) -> BankAccountModel:

        # print(50*"-")
        # print("ACC REPO UPDATE METH BEFORE MERGE")
        # for i in self._session.identity_map.values():
        #     print(i)
        #     print("TRANSIENT", inspect(i).transient)
        #     print("PENDING", inspect(i).pending)
        #     print("PERSISTENT", inspect(i).persistent)
        #     print("DELETED", inspect(i).deleted)
        #     print("DETACHED", inspect(i).detached)
        # IN THIS CASE THE :param: "account" is the new object for this session,
        # and it is having no state relative to the current session (only "transient").
        # so :meth: "merge" hit the database to get the current state of
        # obj "BankAccountModel" with primary key established in :param: "account",
        # then merging will update the entry with this primary key.
        account = await self._session.merge(account)
        print("ACC REPO UPDATE METH AFTER MERGE")
        print("TRANSIENT", inspect(account).transient)
        print("PENDING", inspect(account).pending)
        print("PERSISTENT", inspect(account).persistent)
        print("DELETED", inspect(account).deleted)
        print("DETACHED", inspect(account).detached)
        # for i in self._session.identity_map.values():
        #     print(i)
        #     print("TRANSIENT", inspect(i).transient)
        #     print("PENDING", inspect(i).pending)
        #     print("PERSISTENT", inspect(i).persistent)
        #     print("DELETED", inspect(i).deleted)
        #     print("DETACHED", inspect(i).detached)
        # print(50*"-")
        # await self._session.flush()
        # await self._session.refresh(account)
        return account
