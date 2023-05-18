from typing import Optional

from common.uow import UnitOfWork
from common.database.models import *


class AltAccountService:

    # TODO args? attributes?
    def __init__(self, account_dto: BankAccountRead, uow: UnitOfWork):
        self._account_data = account_dto
        self._uow = uow

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)

    async def account_by_id(self, account_id: int) -> Optional[BankAccountRead]:
        account = await self._uow.account_repo.get_by_id(obj_id=account_id)
        if not account:
            raise Exception("Account does not already exist")
        return self._from_orm_to_dto(input_data=account,
                                     output_model=BankAccountRead)

    async def account_update(self, update_data):

        ...
