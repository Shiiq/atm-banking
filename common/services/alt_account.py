from typing import Optional

from common.uow import UnitOfWork
from common.database.models import *


class AltAccountService:

    # TODO args? attributes?
    def __init__(self, customer_dto: BankCustomerFromDB, uow: UnitOfWork):
        self._account_id = customer_dto.bank_account_id
        self._uow = uow

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)

    async def get_by_id(self, account_id: int) -> Optional[BankAccountModel]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_id)
        return account

    async def update(self, update_data):
        ...
