from typing import Protocol, Optional
from uuid import UUID

from src.infrastructure.database.models import BankCustomerModel


class ICustomerRepo(Protocol):

    async def create(
            self,
            customer: BankCustomerModel
    ) -> BankCustomerModel:
        ...

    async def get_by_id(
            self,
            customer_id: UUID
    ) -> Optional[BankCustomerModel]:
        ...

    async def get_by_fullname(
            self,
            customer_first_name: str,
            customer_last_name: str
    ) -> Optional[BankCustomerModel]:
        ...
