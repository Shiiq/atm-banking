from application.exceptions import CustomerNotExist
from application.services import (AccountService,
                                  CustomerService,
                                  OperationService)
from infrastructure.database.models import dto
from infrastructure.unit_of_work import UnitOfWork


class _Deposit:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)

    async def __call__(self, input_data: dto.DepositInput):
        # input_data = dto.DepositInput(
        #     customer=dto.CustomerInput(first_name="jaks",
        #                                last_name="korspe"),
        #     operation=dto.OperationInput(type_="deposit",
        #                                  amount=1000)
        # )
        async with self.uow:
            try:
                customer_search_data = dto.BankCustomerSearch(
                    first_name=input_data.customer.first_name,
                    last_name=input_data.customer.last_name
                )
                customer = await self._customer_service.customer_by_fullname(
                    customer_search_data=customer_search_data
                )
            except CustomerNotExist(
                    first_name=input_data.customer.first_name,
                    last_name=input_data.customer.last_name
            ) as err:
                # logging err
                customer_create_data = dto.BankCustomerCreate()
                new_customer = await self._customer_service.customer_create(
                    customer_create_data=)

            pass
        pass

    async def _register_customer(self):
        pass

    async def _get_current_customer(self, customer_search_data: dto.BankCustomerSearch):
        customer = await self._customer_service.customer_by_fullname(
            customer_search_data=customer_search_data
        )
        pass

    async def _update_bank_account(self):
        pass

    async def _register_bank_operation(self):
        pass
