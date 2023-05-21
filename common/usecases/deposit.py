from common.database.models import *
from common.services import AccountService, CustomerService, OperationService


class Deposit:

    # processing deposit operation
    # input_data
    #     customer: CustomerDTO | BankCustomerRead
    #     operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    #     amount: PositiveInt = 1000

    def __init__(self, deposit_operation_dto: DepositDTO):
        self._deposit_operation_dto = deposit_operation_dto
        self._account_service = ...
        self._customer_service = ...
        self._operation_service = ...

    async def update_account_balance(self):
        current_balance = ...
        ...
