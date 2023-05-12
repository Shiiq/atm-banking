from typing import Optional

from common.database.models import BankCustomerModel, BankCustomerBaseDTO, BankCustomerToDB, BankCustomerFromDB


class CustomerService:

    def __init__(self, customer_dto: BankCustomerBaseDTO):
        self._customer_dto = customer_dto
        self._session = ...
        self._customer_repo = ...
        self._account_repo = ...

    def _from_dto_to_orm(self, input, output):
        return output(**input.dict())

    def _from_orm_to_dto(self, input, output):
        return output.from_orm(input)

    # TODO args?
    async def _get_or_none_current_customer(self) -> Optional[BankCustomerModel]:
        customer = await self._customer_repo.get_by_fullname(first_name=self._customer_dto.first_name,
                                                             last_name=self._customer_dto.last_name)
        return customer

    # TODO args?
    async def _register_new_customer(self) -> BankCustomerModel:
        customer_dto = BankCustomerToDB(**self._customer_dto.dict())
        customer_orm = self._from_dto_to_orm(input=customer_dto,
                                             output=BankCustomerModel)
        customer = await self._customer_repo.add(customer_orm)
        return customer

    # TODO args?, returning?[orm or dto]
    async def get_or_register_customer(self) -> ...:
        customer_orm = await self._get_or_none_current_customer()
        if not customer_orm:
            customer_orm = await self._register_new_customer()
        return self._from_orm_to_dto(input=customer_orm,
                                     output=BankCustomerFromDB)
