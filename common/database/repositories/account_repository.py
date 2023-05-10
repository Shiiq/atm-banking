from sqlalchemy import select

from common.database.models import BankAccountModel
from common.database.repositories.abstract_repository import (ProtocolRepository,ConnHolder)


class AccountRepository(ConnHolder, ProtocolRepository):

    async def add(self, account: BankAccountModel):
        self._session.add(account)
        await self._session.flush((account,))
        return account

    async def get_by_id(self, account_id: int):
        query = (select(BankAccountModel)
                 .where(BankAccountModel.id == account_id))
        account = await self._session.execute(query)
        return account.scalars().first()

    async def update(self, account: BankAccountModel):
        pass

    async def delete(self, account_id: int):
        pass
