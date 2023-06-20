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
        async with self.uow:
            customer = await ...
            pass
        pass

    async def __register_customer(self):
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
