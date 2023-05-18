from typing import Optional

from common.uow import UnitOfWork
from common.database.models import *


class AltCustomerService:

    # TODO args? attributes?
    def __init__(self, customer_dto: CustomerDTO, uow: UnitOfWork):
        self._customer_data = customer_dto
        self._uow = uow

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)

    async def customer_by_id(self, customer_id: int) -> Optional[BankCustomerRead]:
        customer = await self._uow.customer_repo.get_by_id(obj_id=customer_id)
        if not customer:
            raise Exception("Customer does not exist")
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def customer_by_fullname(self) -> Optional[BankCustomerRead]:
        customer = await self._uow.customer_repo.get_by_fullname(first_name=self._customer_data.first_name,
                                                                 last_name=self._customer_data.last_name)
        if not customer:
            raise Exception("Customer does not exist")
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def customer_create(self) -> BankCustomerRead:
        default_account_dto = AccountDTO()
        account_orm = self._from_dto_to_orm(input_data=default_account_dto,
                                            output_model=BankAccountModel)
        customer_orm = self._from_dto_to_orm(input_data=self._customer_data,
                                             output_model=BankCustomerModel)
        customer_orm.bank_account = account_orm

        customer = await self._uow.customer_repo.create(customer_orm)
        await self._uow.commit()

        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)
