from typing import Optional

from application.exceptions import AccountIDNotExist
from application.dto import (BankAccountRead,
                             BankAccountUpdate,
                             BankAccountSearch)
from infrastructure.database.repositories import IAccountRepo
from .data_converter import DataConverterMixin


class AccountService(DataConverterMixin):

    def __init__(self, account_repo: IAccountRepo):
        self.account_repo = account_repo

    async def by_id(self, search_data: BankAccountSearch) -> Optional[BankAccountRead]:
        account = await self.account_repo.get_by_id(account_id=search_data.id)
        if not account:
            raise AccountIDNotExist(account_id=search_data.id)
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def update(self, update_data: BankAccountUpdate) -> BankAccountRead:
        account = await self.account_repo.get_by_id(account_id=update_data.id)
        account.balance = update_data.balance
        account = await self.account_repo.update(account=account)
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)
