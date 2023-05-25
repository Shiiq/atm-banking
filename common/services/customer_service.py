from typing import Optional

from common.database.models.db import *
from common.database.models.dto import *
from ._base_service import BaseService


class CustomerService(BaseService):

    async def customer_create(self, customer_create_data: BankCustomerCreate) -> BankCustomerRead:
        account_orm = self._from_dto_to_orm(input_data=customer_create_data.bank_account,
                                            output_model=BankAccountModel)
        customer_orm = self._from_dto_to_orm(input_data=customer_create_data.customer,
                                             output_model=BankCustomerModel)
        customer_orm.bank_account = account_orm
        customer = await self._uow.customer_repo.create(customer_orm)
        await self._uow.commit()
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def customer_by_id(self, customer_search_data) -> Optional[BankCustomerRead]:
        customer = await self._uow.customer_repo.get_by_id(
            obj_id=customer_search_data.id
        )
        if not customer:
            raise ValueError("Customer does not exist")
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    # async def customer_by_account_id(self, customer_search_data) -> BankCustomerRead:
    #     customer = await self._uow.customer_repo.get_by_account_id(
    #         obj_id=customer_search_data.bank_account_id
    #     )
    #     return self._from_orm_to_dto(input_data=customer,
    #                                  output_model=BankCustomerRead)

    async def customer_by_fullname(self, customer_search_data) -> Optional[BankCustomerRead]:
        customer = await self._uow.customer_repo.get_by_fullname(
            first_name=customer_search_data.first_name,
            last_name=customer_search_data.last_name
        )
        if not customer:
            raise ValueError("Customer does not exist")
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)
