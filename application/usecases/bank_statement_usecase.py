from infrastructure.database.models import dto
from infrastructure.unit_of_work import UnitOfWork
from ._base_usecase import BaseUsecase


class BankStatement(BaseUsecase):

    def __init__(self, uow: UnitOfWork):
        super().__init__(uow=uow)
        # self.uow = uow
        # self._account_service = AccountService(uow=uow)
        # self._customer_service = CustomerService(uow=uow)
        # self._operation_service = OperationService(uow=uow)

    async def __call__(
            self,
            input_data: dto.BankStatementInput
    ):
        async with self.uow:
            customer_search_data = dto.BankCustomerSearch(first_name=input_data.first_name,
                                                          last_name=input_data.last_name)
            customer = await self._customer_service.by_fullname(search_data=customer_search_data)

            operations_search_data = dto.BankOperationSearch(bank_account_id=customer.bank_account_id,
                                                             bank_customer_id=customer.id,
                                                             since=input_data.since,
                                                             till=input_data.till)
            operations = await self._operation_service.by_date_interval(search_data=operations_search_data)

            return dto.BankOperationsInfo(customer=customer,
                                          since=input_data.since,
                                          till=input_data.till,
                                          operations=operations)
