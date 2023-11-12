from typing import Protocol
from uuid import UUID

from src.infrastructure.database.models import BankAccountModel


class IAccountRepo(Protocol):

    async def get_by_id(self, account_id: UUID) -> BankAccountModel:
        ...

    async def update(self, account: BankAccountModel) -> BankAccountModel:
        ...
