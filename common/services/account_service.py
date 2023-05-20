from typing import Optional

from common.unit_of_work import UnitOfWork
from common.database.models import *

from ._base_service import BaseService


class AccountService(BaseService):

    # TODO args? attributes?
    def __init__(self, account_dto: BankAccountRead, uow: UnitOfWork):
        self._account_data = account_dto
        self._uow = uow

    async def account_by_id(self, account_id: int) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_id)
        if not account:
            raise Exception("Account does not already exist")
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def account_update(self, update_data):

        ...
