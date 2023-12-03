from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from atm.application.interfaces import IAccountRepo
from atm.infrastructure.database.models import BankAccountModel


class AccountRepo(IAccountRepo):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(
            self,
            account_id: UUID
    ) -> Optional[BankAccountModel]:

        query = (
            select(BankAccountModel)
            .where(BankAccountModel.id == account_id)
            .with_for_update()
        )
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
