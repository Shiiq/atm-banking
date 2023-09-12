from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

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
            account_id: UUID
    ) -> Optional[BankAccountModel]:

        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == account_id)
                 .with_for_update())
        account = await self._session.execute(query)
        return account.scalars().first()

    async def update(
            self,
            account: BankAccountModel
    ) -> BankAccountModel:

        # IN THIS CASE THE :param: "account" is the new object for this session,
        # and it is having no state relative to the current session (only "transient").
        # so :meth: "merge" hit the database to get the current state of
        # obj "BankAccountModel" with primary key established in :param: "account",
        # then merging will update the entry with this primary key.
        account = await self._session.merge(account)
        return account
