from typing import Optional

from common.unit_of_work import UnitOfWork
from common.database.models.db import *
from common.database.models.dto import *
# from common.database.models import *

from ._base_service import BaseService


class AccountService(BaseService):

    # TODO args? attributes?
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def account_create(self, account_create_data):
        ...

    async def account_by_id(self, account_search_data) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_search_data.id)
        # if not account:
        #     raise Exception("Account does not already exist")
        return account

    async def account_update(self, account_update_data: BankAccountUpdate) -> BankAccountRead:
        account = await self._uow.account_repo.get_by_id(obj_id=account_update_data.id)
        account.balance = account_update_data.balance
        account = await self._uow.account_repo.update(obj=account)
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)
