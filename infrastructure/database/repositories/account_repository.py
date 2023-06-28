from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.database.models.db import BankAccountModel
from .sa_repository import SARepo
from ._base_repository import ProtocolRepo


class AccountRepository(SARepo, ProtocolRepo):

    async def create(self, obj: BankAccountModel) -> BankAccountModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_by_id(self, obj_id: int) -> Optional[BankAccountModel]:
        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == obj_id)
                 .with_for_update()
                 .options(joinedload(BankAccountModel.customer)))
        account = await self._session.execute(query)
        return account.scalars().first()

    async def update(self, obj: BankAccountModel):
        await self._session.flush()
        await self._session.refresh(obj)
        return obj
