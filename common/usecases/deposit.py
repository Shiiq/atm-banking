from common.database.models.constants import BankOperationsToDB
from common.database.models.db import *
from common.database.models.dto import *

from common.services import AccountService, CustomerService, OperationService


class Deposit:

    def __init__(self, deposit_operation_dto: DepositInputDTO, uow):
        self._input_data = deposit_operation_dto
        self._summary_data = SummaryOperationInfo(customer=None,
                                                  operation=None)
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)

    async def __call__(self):
        await self._get_customer()
        await self._update_account()
        await self._register_operation()
        print(self._summary_data)

    async def _get_customer(self):
        try:
            customer = await self._customer_service.customer_by_fullname(customer_data=self._input_data.customer)
        except Exception:
            register_data = BankCustomerCreate(customer=self._input_data.customer)
            customer = await self._customer_service.customer_create(customer_data=register_data)
        self._summary_data.customer = customer

    async def _update_account(self):
        current_account_data = await self._account_service.account_by_id(account_id=self._summary_data.customer.bank_account_id)
        balance = current_account_data.balance
        balance += self._input_data.amount
        update_data = BankAccountUpdate(id=self._summary_data.customer.bank_account_id,
                                        balance=balance)
        updated_account = await self._account_service.account_update(update_account_data=update_data)
        self._summary_data.customer.bank_account = updated_account

    async def _register_operation(self):
        register_data = BankOperationCreate(amount=self._input_data.amount,
                                            bank_account_id=self._summary_data.customer.bank_account_id,
                                            bank_customer_id=self._summary_data.customer.id,
                                            bank_operation=BankOperationsToDB.DEPOSIT)
        operation = await self._operation_service.operation_create(operation_data=register_data)
        self._summary_data.operation = operation
