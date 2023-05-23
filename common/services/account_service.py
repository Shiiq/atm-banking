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

    async def account_create(self, account_data):
        ...

    async def account_by_id(self, account_id: int) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_id)
        if not account:
            raise Exception("Account does not already exist")
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    #TODO redesign
    async def account_update(self, update_account_data: BankAccountUpdate) -> BankAccountRead:
        account_dto = await self.account_by_id(update_account_data.id)
        account_dto.balance = update_account_data.balance
        account_orm = self._from_dto_to_orm(input_data=account_dto,
                                            output_model=BankAccountModel)
        account = await self._uow.account_repo.update(account_orm)
        await self._uow.commit()
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)
