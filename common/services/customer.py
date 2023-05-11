from typing import Optional

from common.database.models import BankCustomerModel, BankCustomerDTO


class CustomerService:

    def __init__(self, customer_dto: BankCustomerDTO):
        self.customer_dto = customer_dto
        self.session = ...
        self.customer_repo = ...

    # TODO fix, args?
    def _from_dto_to_orm(self) -> BankCustomerModel:
        return BankCustomerModel(**self.customer_dto.dict())

    # TODO fix, args?, returning?
    def _from_orm_to_dto(self) -> ...:
        pass

    # TODO args?
    async def _get_or_none_current_customer(self) -> Optional[BankCustomerModel]:
        c = await self.customer_repo.get_by_fullname(first_name=self.customer_dto.first_name,
                                                     last_name=self.customer_dto.last_name)
        return c

    # TODO args?
    async def _register_new_customer(self) -> BankCustomerModel:
        c_orm = self._from_dto_to_orm()
        c = await self.customer_repo.add(c_orm)
        return c

    # TODO args?, returning?[orm or dto]
    async def get_or_register_customer(self) -> ...:
        c = await self._get_or_none_current_customer()
        if not c:
            c = await self._register_new_customer()
        return c
