from common.database.models.constants import BankOperationsToDB, BankOperationsFromInput
from common.database.models.dto import *
from common.services import AccountService, CustomerService, OperationService


class Deposit:

    def __init__(self, uow):
        self._input_data: DepositInput = DepositInput(
            customer=CustomerInput(first_name="Chuck",
                                   last_name="Buzz"),
            operation=OperationInput(type_=BankOperationsFromInput.DEPOSIT,
                                     amount=100500)
        )
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)

    async def __call__(self, input_data: DepositInput):
        customer_data = input_data.customer
        operation_data = input_data.operation

        customer = await self._get_customer(customer_data=customer_data)
        bank_account_data = customer.bank_account

        bank_account = await self._update_bank_account(bank_account_data=bank_account_data,
                                                       operation_data=operation_data)

    async def _register_customer(self, customer_data: CustomerInput):
        customer = await self._customer_service.customer_create(
            customer_create_data=BankCustomerCreate(customer=customer_data)
        )
        # commit
        return customer

    async def _get_customer(self, customer_data: CustomerInput) -> BankCustomerRead:
        customer = await self._customer_service.customer_by_fullname(
            customer_search_data=BankCustomerSearch(first_name=customer_data.first_name,
                                                    last_name=customer_data.last_name)
        )
        if not customer:
            customer = await self._register_customer(customer_data=customer_data)
        return customer

    async def _update_bank_account(self, bank_account_data: BankAccountRead, operation_data: OperationInput, through_customer=False):
        updated_balance = bank_account_data.balance + operation_data.amount
        bank_account = await self._account_service.account_update(
            account_update_data=BankAccountUpdate(id=bank_account_data.id,
                                                  balance=updated_balance)
        )
        if through_customer:
            customer = await self._customer_service.customer_by_account_id(
                customer_search_data=BankCustomerSearch(bank_account_id=bank_account_data.id)
            )
            return customer
        return bank_account

    async def _register_operation(self):
        pass
