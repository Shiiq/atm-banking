from typing import Optional

from common.uow import UnitOfWork
from common.database.models import *


class CustomerService:
    """The task of the 'Customer Service' is to get the data
    of the current bank customer, or add it to database with zero bank account
    and returning a new bank customer."""

    # TODO args? attributes?
    def __init__(self, customer_dto: CustomerDTO, uow: UnitOfWork):
        self._input_customer_data = customer_dto
        self._uow = uow

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)

    async def _get_or_none_current_customer(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        customer = await self._uow.customer_repo.get_by_fullname(first_name=first_name,
                                                                 last_name=last_name)
        return customer

    async def _register_new_customer(self) -> BankCustomerModel:
        default_account_dto = AccountDTO()

        customer_orm = self._from_dto_to_orm(input_data=self._input_customer_data,
                                             output_model=BankCustomerModel)
        account_orm = self._from_dto_to_orm(input_data=default_account_dto,
                                            output_model=BankAccountModel)

        customer_orm.bank_account = account_orm
        customer = await self._uow.customer_repo.add(customer_orm)
        await self._uow.commit()
        return customer

    async def get_or_register_customer(self) -> BankCustomerRead:
        customer_orm = await self._get_or_none_current_customer(self._input_customer_data.first_name,
                                                                self._input_customer_data.last_name)
        if not customer_orm:
            customer_orm = await self._register_new_customer()
        return self._from_orm_to_dto(input_data=customer_orm,
                                     output_model=BankCustomerRead)
