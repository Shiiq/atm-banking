from common.database.models import *


class DepositUseCase:

    # processing deposit operation

    def __init__(self):
        self._deposit_operation_dto: DepositDTO = ...

    async def check_account_balance(self):
        ...
