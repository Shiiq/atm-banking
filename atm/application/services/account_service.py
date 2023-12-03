from uuid import UUID

from atm.application.dto import BankAccountRead
from atm.application.dto import BankAccountUpdate
from atm.application.exceptions import AccountIDNotExist
from atm.application.interfaces import IAccountRepo
from atm.infrastructure.database.models import BankAccountModel
from .data_converter import DataConverterMixin


class AccountService(DataConverterMixin):

    def __init__(self, account_repo: IAccountRepo):
        self.account_repo = account_repo

    async def get_by_id(self, account_id: UUID) -> BankAccountRead:

        account = await self.account_repo.get_by_id(account_id=account_id)
        if not account:
            raise AccountIDNotExist(account_id=account_id)
        return self.from_orm_to_dto(
            input_data=account,
            output_model=BankAccountRead
        )

    async def update(self, update_data: BankAccountUpdate) -> BankAccountRead:

        account_orm = self.from_dto_to_orm(
            input_data=update_data,
            output_model=BankAccountModel
        )
        updated_account_orm = await self.account_repo.update(
            account=account_orm
        )
        return self.from_orm_to_dto(
            input_data=updated_account_orm,
            output_model=BankAccountRead
        )
