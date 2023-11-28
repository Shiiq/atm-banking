from datetime import datetime
from typing import Protocol, Sequence
from uuid import UUID

from atm_banking.infrastructure.database.models import BankOperationModel


class IOperationRepo(Protocol):

    async def create(
            self,
            operation: BankOperationModel
    ) -> BankOperationModel:
        ...

    async def get_by_date_interval(
            self,
            account_id: UUID,
            customer_id: UUID,
            start_date: datetime,
            end_date: datetime
    ) -> Sequence[BankOperationModel]:
        ...
