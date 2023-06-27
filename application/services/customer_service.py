from typing import Optional

from application.exceptions import CustomerNotExist, CustomerIDNotExist
from infrastructure.database.models.db import (BankAccountModel,
                                               BankCustomerModel)
from infrastructure.database.models.dto import (BankCustomerCreate,
                                                BankCustomerRead,
                                                BankCustomerSearch)
from ._base_service import BaseService


class CustomerService(BaseService):

    async def create(self, create_data: BankCustomerCreate) -> BankCustomerRead:
        account_orm = self._from_dto_to_orm(input_data=create_data.bank_account,
                                            output_model=BankAccountModel)
        customer_orm = self._from_dto_to_orm(input_data=create_data.customer,
                                             output_model=BankCustomerModel)
        customer_orm.bank_account = account_orm
        customer = await self._uow.customer_repo.create(customer_orm)
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def by_id(self, search_data: BankCustomerSearch) -> Optional[BankCustomerRead]:
        customer = await self._uow.customer_repo.get_by_id(
            obj_id=search_data.id
        )
        if not customer:
            raise CustomerIDNotExist(customer_id=search_data.id)
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def by_fullname(self, search_data: BankCustomerSearch) -> Optional[BankCustomerRead]:
        customer = await self._uow.customer_repo.get_by_fullname(
            first_name=search_data.first_name,
            last_name=search_data.last_name
        )
        if not customer:
            raise CustomerNotExist(first_name=search_data.first_name,
                                   last_name=search_data.last_name)
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def update(self):
        pass

    async def delete(self):
        pass
