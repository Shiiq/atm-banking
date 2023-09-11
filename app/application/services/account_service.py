from typing import Optional

from app.application.dto import (BankAccountRead,
                                 BankAccountUpdate,
                                 BankAccountSearch)
from app.application.exceptions import AccountIDNotExist
from app.infrastructure.database.repositories import IAccountRepo
from app.infrastructure.database.models import BankAccountModel
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

    # async def update(self, update_data: BankAccountUpdate) -> BankAccountRead:
    #     account = await self.account_repo.get_by_id(account_id=update_data.id)
    #     account.balance = update_data.balance
    #     account = await self.account_repo.update(account=account)
    #     return self._from_orm_to_dto(input_data=account,
    #                                  output_model=BankAccountRead)

    # async def update(self, updated_account: BankAccountRead) -> BankAccountRead:
    async def update(self, updates_for_account) -> BankAccountRead:
        account_to_orm = BankAccountModel(
            id=updates_for_account.id,
            balance=updates_for_account.balance
        )
        updated_account_orm = await self.account_repo.update(account=account_to_orm)
        return self._from_orm_to_dto(input_data=updated_account_orm,
                                     output_model=BankAccountRead)
