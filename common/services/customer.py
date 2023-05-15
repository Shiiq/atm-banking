from typing import Optional

from common.uow import UnitOfWork
from common.database.models import (AccountBaseDTO,
                                    CustomerBaseDTO,
                                    BankAccountModel,
                                    BankCustomerModel,
                                    BankCustomerToDB,
                                    BankCustomerFromDB)


class CustomerService:

    # TODO args? attributes?
    def __init__(self, customer_dto: CustomerBaseDTO, uow: UnitOfWork):
        self._input_customer_data = customer_dto
        self._uow = uow

    # TODO annotations? args?
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations? args?
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)

    async def _get_or_none_current_customer(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        customer = await self._uow.customer_repo.get_by_fullname(first_name=first_name,
                                                                 last_name=last_name)
        return customer

    async def _register_new_customer(self, first_name: str, last_name: str) -> BankCustomerModel:
        customer_dto = BankCustomerToDB(first_name=first_name,
                                        last_name=last_name)
        account_dto = AccountBaseDTO()

        customer_orm = self._from_dto_to_orm(input_data=customer_dto,
                                             output_model=BankCustomerModel)
        account_orm = self._from_dto_to_orm(input_data=account_dto,
                                            output_model=BankAccountModel)
        customer_orm.bank_account = account_orm
        customer = await self._uow.customer_repo.add(customer_orm)
        await self._uow.commit()
        return customer

    async def get_or_register_customer(self) -> BankCustomerFromDB:
        customer_orm = await self._get_or_none_current_customer(self._input_customer_data.first_name,
                                                                self._input_customer_data.last_name)
        if not customer_orm:
            customer_orm = await self._register_new_customer(self._input_customer_data.first_name,
                                                             self._input_customer_data.last_name)
        return self._from_orm_to_dto(input_data=customer_orm,
                                     output_model=BankCustomerFromDB)
