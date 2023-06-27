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

    async def __call__(
            self,
            input_data: dto.DepositInput
    ):
        # input_data = dto.DepositInput(
        #     customer=dto.CustomerInput(first_name="jaks",
        #                                last_name="korspe"),
        #     operation=dto.OperationInput(type_="deposit",
        #                                  amount=1000)
        # )
        async with self.uow:

            try:
                customer_search_data = dto.BankCustomerSearch(first_name=input_data.customer.first_name,
                                                              last_name=input_data.customer.last_name)
                customer = await self._customer_service.by_fullname(customer_search_data=customer_search_data)

            except CustomerNotExist(first_name=input_data.customer.first_name,
                                    last_name=input_data.customer.last_name) as err:
                # logging err
                customer_create_data = dto.BankCustomerCreate(first_name=input_data.customer.first_name,
                                                              last_name=input_data.customer.last_name)
                customer = await self._customer_service.create(customer_create_data=customer_create_data)
                # logging creation

            account_search_data = dto.BankAccountSearch(id=customer.bank_account_id)
            current_account = await self._account_service.by_id(account_search_data=account_search_data)
            account_update_data = dto.BankAccountUpdate(id=current_account.id,
                                                        balance=(current_account.balance + input_data.operation.amount))


    def update_current_balance_data(
            self,
            account_search_data: dto.BankAccountSearch,
            operation_data: dto.OperationInput
    ) -> dto.BankAccountRead:
        updated_balance = account.balance + deposit_value
        return updated_balance
