from common.database.models.constants import BankOperationsToDB
from common.database.models import *
from common.database.models.db import *
from common.database.models.dto import BankOperationCreate, BankOperationRead

from common.services import AccountService, CustomerService, OperationService


class Deposit:

    # processing deposit operation
    # input_data
    #     customer: CustomerDTO | BankCustomerRead
    #         before identification  after identification
    #     operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    #     amount: PositiveInt = 1000

    def __init__(self, deposit_operation_dto: DepositDTO, uow):
        self._deposit_data = deposit_operation_dto
        # self._account_service = AccountService(uow=uow)
        self._account_service: AccountService = ...
        # self._customer_service = CustomerService(uow=uow)
        self._customer_service: CustomerService = ...
        # self._operation_service = OperationService(uow=uow)
        self._operation_service: OperationService = ...
        # self._output_dto = ...

    async def __call__(self):
        # update self customer information by getting it from db or register new
        await self._get_or_register_customer()
        # update bank account balance data
        ...
        # register bank operation to db
        pass

    async def _get_or_register_customer(self):
        try:
            customer = await self._customer_service.customer_by_fullname(customer_data=self._deposit_data.customer)
        except Exception:
            # logging("Customer does not exist")
            pass
        finally:
            customer = await self._customer_service.customer_create(customer_data=self._deposit_data.customer)
            # logging("Customer {customer.id} is registered")
            self._deposit_data.customer = customer

    async def _update_bank_account_balance(self):
        account_update_data = BankAccountUpdate(id=self._deposit_data.customer.bank_account_id,
                                                amount=self._deposit_data.amount)
        updated_account = await self._account_service.account_update(account_update_data=account_update_data)
        # logging("Account {updated_account.id} balance is updated")
        self._deposit_dto.customer.bank_account = updated_account

    async def _register_deposit_operation_to_db(self):
        deposit_operation_data = BankOperationCreate(amount=self._deposit_dto.amount,
                                                     bank_account_id=self._deposit_dto.customer.bank_account_id,
                                                     bank_customer_id=self._deposit_dto.customer.id,
                                                     bank_operation=BankOperationsToDB.DEPOSIT)
        operation = await self._operation_service.operation_create(operation_data=deposit_operation_data)

        ...