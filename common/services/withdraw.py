from common.database.models import BankCustomerFromDB, DepositDTO
from common.uow import UnitOfWork


class WithdrawOperationService:

    def __init__(self, customer_dto: BankCustomerFromDB, operation_dto: DepositDTO, uow: UnitOfWork):
        self._customer_data = customer_dto
        self._input_operation_data = operation_dto
        self._uow = uow

    async def get_current_account_deposit(self):
        pass