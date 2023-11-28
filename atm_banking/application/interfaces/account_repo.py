from typing import Protocol, Optional
from uuid import UUID

from atm_banking.infrastructure.database.models import BankAccountModel


class IAccountRepo(Protocol):

    async def get_by_id(self, account_id: UUID) -> Optional[BankAccountModel]:
        ...

    async def update(self, account: BankAccountModel) -> BankAccountModel:
        ...
