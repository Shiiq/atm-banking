from typing import Optional

from infrastructure.database.models.dto import (BankAccountCreate,
                                                BankAccountRead,
                                                BankAccountUpdate,
                                                BankAccountSearch)
from ._base_service import BaseService


class AccountService(BaseService):

    async def account_create(self, account_create_data: BankAccountCreate):
        pass

    async def account_by_id(self, account_search_data: BankAccountSearch) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_search_data.id)
        print("account_update", dir(account))
        if not account:
            # TODO custom exceptions
            raise ValueError("Account does not already exist")
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def account_update(self, account_update_data: BankAccountUpdate) -> BankAccountRead:
        account = await self._uow.account_repo.get_by_id(obj_id=account_update_data.id)
        account.balance = account_update_data.balance
        account = await self._uow.account_repo.update(obj=account)
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def account_delete(self):
        pass
