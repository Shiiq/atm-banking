from typing import Optional

from common.database.models.db import *
from common.database.models.dto import *
from ._base_service import BaseService


class AccountService(BaseService):

    async def account_create(self, account_create_data: BankAccountCreate):
        ...

    async def account_by_id(self, account_search_data: BankAccountSearch) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_search_data.id)
        print("account_update", dir(account))
        if not account:
            raise ValueError("Account does not already exist")
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def account_update(self, account_update_data: BankAccountUpdate) -> BankAccountRead:
        account = await self._uow.account_repo.get_by_id(obj_id=account_update_data.id)
        account.balance = account.balance + account_update_data.amount
        account = await self._uow.account_repo.update(obj=account)
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)
