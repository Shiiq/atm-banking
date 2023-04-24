from common.database.core import session_factory
from common.database.db_models import BankAccountModel, BankClientModel, BankOperationModel
from common.database.dto_models import BankStatementDTO, DepositOrWithdrawDTO
from common.database.repository import BankClientRepository


class DepositOrWithdrawService:

    def __init__(self, data: DepositOrWithdrawDTO, session_factory):
        self._session = session_factory
        self._data = data
        self._bank_repository = BankClientRepository()

    async def register(self, session, bank_client):
        client = await self._bank_repository.add(session, bank_client)


    async def get_or_register(self):
        client = await self._bank_repository.get_by_full_name_or_none()


    def create_entity(self, data):
        client = BankClientModel(first_name=data.first_name,
                                 last_name=data.last_name)
        account = BankAccountModel(holder=client)
        pass

    async def create_bank_client(self):
        pass

    async def create_bank_account(self):
        pass