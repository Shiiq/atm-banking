from typing import Optional

from common.database.models import (BankAccountModel,
                                    BankCustomerModel,
                                    CustomerBaseDTO,
                                    BankCustomerToDB,
                                    BankCustomerFromDB,
                                    AccountBaseDTO)


class CustomerService:

    # TODO args? attributes?
    def __init__(self, customer_dto: CustomerBaseDTO):
        self._input_customer_data = customer_dto
        self._session = ...
        self._customer_repo = ...
        self._account_repo = ...
        self._uow = ...

    # TODO annotations?
    def _from_dto_to_orm(self, input, output):
        return output(**input.dict())

    # TODO annotations?
    def _from_orm_to_dto(self, input, output):
        return output.from_orm(input)

    async def _get_or_none_current_customer(self, first_name: str, last_name: str) -> Optional[BankCustomerModel]:
        customer = await self._customer_repo.get_by_fullname(first_name=first_name,
                                                             last_name=last_name)
        return customer

    async def _register_new_customer(self, first_name: str, last_name: str) -> BankCustomerModel:
        customer_dto = BankCustomerToDB(first_name=first_name,
                                        last_name=last_name)
        account_dto = AccountBaseDTO()

        customer_orm = self._from_dto_to_orm(input=customer_dto,
                                             output=BankCustomerModel)
        account_orm = self._from_dto_to_orm(input=account_dto,
                                            output=BankAccountModel)
        customer_orm.bank_account = account_orm
        customer = await self._customer_repo.add(customer_orm)
        return customer

    async def get_or_register_customer(self) -> BankCustomerFromDB:
        customer_orm = await self._get_or_none_current_customer(self._input_customer_data.first_name,
                                                                self._input_customer_data.last_name)
        if not customer_orm:
            customer_orm = await self._register_new_customer(self._input_customer_data.first_name,
                                                             self._input_customer_data.last_name)
        return self._from_orm_to_dto(input=customer_orm,
                                     output=BankCustomerFromDB)
