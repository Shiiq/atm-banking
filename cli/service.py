from common.database.models.db_models import BankAccountModel, BankClientModel
from common.database.models.dto_models import DepositOrWithdrawDTO
from common.database.repository import BankClientRepository


class DepositService:

    def __init__(self, data: DepositOrWithdrawDTO):
        self._session = ...
        self._customer_data = data
        self._bank_repository = BankClientRepository()

    async def register(self):
        bank_customer = BankClientModel(
            first_name=self._customer_data.first_name,
            last_name=self._customer_data.last_name
        )
        bank_account = BankAccountModel(
            deposit=self._customer_data.amount,
            holder=bank_customer
        )
        customer = await self._bank_repository.add(
            session=self._session,
            bank_customer=bank_customer,
            bank_account=bank_account
        )
        return customer

    async def get_customer(self):
        return self._bank_repository.get_by_full_name_or_none(
            self._session,
            self._customer_data.first_name,
            self._customer_data.last_name
        )

    async def get_or_register(self):
        customer = await self.get_customer()
        if not customer:
            customer = await self.register()
        return customer

    async def pas(self):
        pass
