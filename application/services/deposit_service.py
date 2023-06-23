from application.exceptions import CustomerIDNotExist, CustomerNotExist
from infrastructure.database.models import db
from infrastructure.database.models import dto

from ._base_service import BaseService


class DepositService(BaseService):

    # def __pipeline__(self):
        # input_data = dto.DepositInput(
        #     customer=dto.CustomerInput(first_name="jaks",
        #                                last_name="korspe"),
        #     operation=dto.OperationInput(type_="deposit",
        #                                  amount=1000)
        # )
        # try to get current customer
        # customer_search_data = dto.BankCustomerSearch(
        #     first_name=input_data.customer.first_name,
        #     last_name=input_data.customer.last_name
        # )
        # try:
        #     c = await self.get_customer(customer_search_data)
        # except CustomerNotExist:
        #     customer_create_data = dto.BankCustomerCreate(
        #         first_name=input_data.customer.first_name,
        #         last_name=input_data.customer.last_name,
        #         # bank_account = 'creates by default'
        #     )
        #     c = await self.register_customer(customer_create_data)


    async def _register_customer(
            self,
            customer_create_data: dto.BankCustomerCreate
    ) -> db.BankCustomerModel:

        customer_orm = db.BankCustomerModel(
            first_name=customer_create_data.first_name,
            last_name=customer_create_data.last_name,
            bank_account=db.BankAccountModel()

        )
        customer = await self._uow.customer_repo.create(customer_orm)
        return customer

    async def get_or_register_customer(self, customer_search_data) -> db.BankCustomerModel:
        try:
            customer = await self._uow.customer_repo.get_by_fullname(
                first_name=customer_search_data.first_name,
                last_name=customer_search_data.last_name
            )
        except CustomerNotExist:
            customer_create_data = dto.BankCustomerCreate(
                first_name=customer_search_data.first_name,
                last_name=customer_search_data.last_name
            )
            customer = await self._register_customer(
                customer_create_data=customer_create_data
            )
        return customer

    pass
