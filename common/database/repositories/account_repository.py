from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from common.database.models.db import BankAccountModel
from ._base_repository import ProtocolRepo
from .sa_repository import SARepo


class AccountRepository(SARepo, ProtocolRepo):

    async def create(self, obj: BankAccountModel) -> BankAccountModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_by_id(self, obj_id: int) -> Optional[BankAccountModel]:
        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == obj_id)
                 .options(joinedload(BankAccountModel.customer)))
        account = await self._session.execute(query)
        return account.scalars().first()

    async def update(self, obj: BankAccountModel):
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def delete(self, obj_id: int):
        pass
