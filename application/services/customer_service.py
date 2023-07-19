from typing import Optional

from application.exceptions import CustomerNotExist, CustomerIDNotExist
from infrastructure.database.models.db import (BankAccountModel,
                                               BankCustomerModel)
from application.dto import (BankCustomerCreate,
                             BankCustomerRead,
                             BankCustomerSearch)
from infrastructure.database.repositories import ICustomerRepo
from .data_converter import DataConverterMixin


class CustomerService(DataConverterMixin):

    def __init__(self, customer_repo: ICustomerRepo):
        self.customer_repo = customer_repo

    async def create(self, create_data: BankCustomerCreate) -> BankCustomerRead:
        account_orm = self._from_dto_to_orm(input_data=create_data.bank_account,
                                            output_model=BankAccountModel)
        customer_orm = BankCustomerModel(first_name=create_data.first_name,
                                         last_name=create_data.last_name,
                                         bank_account=account_orm)
        customer = await self.customer_repo.create(customer=customer_orm)
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def by_id(self, search_data: BankCustomerSearch) -> Optional[BankCustomerRead]:
        customer = await self.customer_repo.get_by_id(customer_id=search_data.id)
        if not customer:
            raise CustomerIDNotExist(customer_id=search_data.id)
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)

    async def by_fullname(self, search_data: BankCustomerSearch) -> Optional[BankCustomerRead]:
        customer = await self.customer_repo.get_by_fullname(
            customer_first_name=search_data.first_name,
            customer_last_name=search_data.last_name
        )
        if not customer:
            raise CustomerNotExist(first_name=search_data.first_name,
                                   last_name=search_data.last_name)
        return self._from_orm_to_dto(input_data=customer,
                                     output_model=BankCustomerRead)
