from common.database.models import *
from common.services import AccountService, CustomerService, OperationService


class Deposit:

    # processing deposit operation
    # input_data
    #     customer: CustomerDTO | BankCustomerRead
    #         before identification  after identification
    #     operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    #     amount: PositiveInt = 1000

    def __init__(self, deposit_operation_dto: DepositDTO, uow):
        self._deposit_dto = deposit_operation_dto
        # self._account_service = AccountService(uow=uow)
        self._account_service: AccountService = ...
        # self._customer_service = CustomerService(uow=uow)
        self._customer_service: CustomerService = ...
        # self._operation_service = OperationService(uow=uow
        self._operation_service: OperationService = ...

    async def __call__(self):
        # update self customer information by getting it from db or register new
        await self._get_or_register_customer()

        pass

    async def _get_or_register_customer(self):
        try:
            customer = await self._customer_service.customer_by_fullname(customer_data=self._deposit_dto.customer)
        except Exception:
            # logging("Customer does not exist")
            pass
        finally:
            customer = await self._customer_service.customer_create(customer_data=self._deposit_dto.customer)
            # logging("Customer {customer.id} is registered")
            self._deposit_dto.customer = customer

    async def _update_bank_account_balance(self):
        account = await self._account_service.account_by_id(account_id=self._deposit_dto.customer.bank_account_id)
