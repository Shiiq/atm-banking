from sqlalchemy import select

from common.database.models import BankAccountModel
from common.database.repositories.abstract_repository import (ProtocolRepository,ConnHolder)


class AccountRepository(ConnHolder, ProtocolRepository):

    async def add(self, obj: BankAccountModel) -> BankAccountModel:
        self._session.add(obj)
        await self._session.flush()
        return obj

    async def get_by_id(self, obj_id: int):
        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == obj_id))
        account = await self._session.execute(query)
        return account.scalars().first()

    async def update(self, obj: BankAccountModel):
        pass

    async def delete(self, obj_id: int):
        pass
