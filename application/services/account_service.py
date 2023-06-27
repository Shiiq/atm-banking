from typing import Optional

from infrastructure.database.models.dto import (BankAccountCreate,
                                                BankAccountRead,
                                                BankAccountUpdate,
                                                BankAccountSearch)
from ._base_service import BaseService


class AccountService(BaseService):

    async def create(self, create_data: BankAccountCreate):
        pass

    async def by_id(self, search_data: BankAccountSearch) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=search_data.id)
        if not account:
            # TODO custom exceptions
            raise ValueError("Account does not already exist")
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def update(self, update_data: BankAccountUpdate) -> BankAccountRead:
        account = await self._uow.account_repo.get_by_id(obj_id=update_data.id)
        account.balance = update_data.balance
        account = await self._uow.account_repo.update(obj=account)
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def delete(self):
        pass
