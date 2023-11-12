from typing import Optional
from uuid import UUID

from src.application.dto import BankCustomerCreate
from src.application.dto import BankCustomerRead
from src.application.exceptions import CustomerNotExist, CustomerIDNotExist
from src.application.interfaces import ICustomerRepo
from src.infrastructure.database.models import BankAccountModel
from src.infrastructure.database.models import BankCustomerModel
from .data_converter import DataConverterMixin


class CustomerService(DataConverterMixin):

    def __init__(self, customer_repo: ICustomerRepo):
        self.customer_repo = customer_repo

    async def create(
            self,
            create_data: BankCustomerCreate
    ) -> BankCustomerRead:

        account_orm = self.from_dto_to_orm(
            input_data=create_data.bank_account,
            output_model=BankAccountModel
        )
        customer_orm = BankCustomerModel(
            first_name=create_data.first_name,
            last_name=create_data.last_name,
            bank_account=account_orm
        )
        customer = await self.customer_repo.create(customer=customer_orm)
        return self.from_orm_to_dto(
            input_data=customer,
            output_model=BankCustomerRead
        )

    async def get_by_id(
            self,
            customer_id: UUID
    ) -> BankCustomerRead:

        customer = await self.customer_repo.get_by_id(customer_id=customer_id)
        if not customer:
            raise CustomerIDNotExist(customer_id=customer_id)
        return self.from_orm_to_dto(
            input_data=customer,
            output_model=BankCustomerRead
        )

    async def get_by_fullname(
            self,
            customer_first_name: str,
            customer_last_name: str
    ) -> BankCustomerRead:

        customer = await self.customer_repo.get_by_fullname(
            customer_first_name=customer_first_name,
            customer_last_name=customer_last_name
        )
        if not customer:
            raise CustomerNotExist(
                first_name=customer_first_name,
                last_name=customer_last_name
            )
        return self.from_orm_to_dto(
            input_data=customer,
            output_model=BankCustomerRead
        )
