from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.infrastructure.database.models.db import BankAccountModel
from .interfaces import IAccountRepo
from .sa_repository import SARepo


class AccountRepo(SARepo, IAccountRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, account: BankAccountModel) -> BankAccountModel:
        self._session.add(account)
        await self._session.flush()
        return account

    async def get_by_id(self, account_id: int) -> Optional[BankAccountModel]:
        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == account_id)
                 .with_for_update()
                 .options(joinedload(BankAccountModel.customer)))
        account = await self._session.execute(query)
        return account.scalars().first()

    async def update(self, account: BankAccountModel):
        await self._session.flush()
        await self._session.refresh(account)
        return account
