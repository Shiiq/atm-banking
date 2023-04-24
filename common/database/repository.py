from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.database.core import session_factory
from common.database.db_models import BankAccountModel, BankClientModel, BankOperationModel
from common.database.dto_models import DepositOrWithdrawDTO


class BankClientRepository:

    def __init__(self):
        self._session_factory = session_factory

    async def get_by_full_name_or_none(
            self, session: AsyncSession, first_name: str, last_name: str
    ) -> BankClientModel:
        stmt = (select(BankClientModel)
                .where(BankClientModel.first_name == first_name,
                       BankClientModel.last_name == last_name))
        client = await session.execute(stmt)
        return client.scalars().first()


    async def add(
            self, session: AsyncSession, bank_client: BankClientModel
    ) -> BankClientModel:
        session.add(bank_client)
        await session.commit()
        await session.refresh(bank_client)
        return bank_client