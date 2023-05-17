from typing import Optional

from common.uow import UnitOfWork
from common.database.models import *


class AltCustomerService:

    # TODO args? attributes?
    def __init__(self, customer_dto: CustomerBaseDTO, uow: UnitOfWork):
        self._input_customer_data = customer_dto
        self._uow = uow

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)

    async def get_by_id(self, id: int) -> Optional[BankCustomerModel]:
        customer = await self._uow.customer_repo.get_by_id(obj_id=id)
        if not customer:
            raise Exception("Customer does not exist")
        return customer

    async def get_by_fullname(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        customer = await self._uow.customer_repo.get_by_fullname(first_name=first_name,
                                                                 last_name=last_name)
        if not customer:
            raise Exception("Customer does not exist")
        return customer

    # TODO create customer data arg?
    async def register_new_customer(self) -> BankCustomerModel:
        default_account_dto = AccountBaseDTO()

        customer_orm = self._from_dto_to_orm(input_data=self._input_customer_data,
                                             output_model=BankCustomerModel)
        account_orm = self._from_dto_to_orm(input_data=default_account_dto,
                                            output_model=BankAccountModel)

        customer_orm.bank_account = account_orm
        customer = await self._uow.customer_repo.add(customer_orm)
        await self._uow.commit()
        return customer
