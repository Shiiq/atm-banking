from pydantic import TypeAdapter

from app.application.dto import (BankOperationCreate,
                                 BankOperationRead,
                                 BankOperationSearch,
                                 ShortOperationInfo)
from app.infrastructure.database.models import BankOperationModel
from app.infrastructure.database.repositories import IOperationRepo
from .data_converter import DataConverterMixin


class OperationService(DataConverterMixin):

    def __init__(self, operation_repo: IOperationRepo):
        self._list_adapter = TypeAdapter(list[ShortOperationInfo])
        self.operation_repo = operation_repo

    async def create(
            self,
            create_data: BankOperationCreate
    ) -> BankOperationRead:

        operation_orm = self._from_dto_to_orm(
            input_data=create_data,
            output_model=BankOperationModel
        )
        operation = await self.operation_repo.create(
            operation=operation_orm
        )
        return self._from_orm_to_dto(
            input_data=operation,
            output_model=BankOperationRead
        )

    async def by_id(
            self,
            search_data: BankOperationSearch
    ) -> BankOperationRead:

        operation = await self.operation_repo.get_by_id(
            operation_id=search_data.id
        )
        return self._from_orm_to_dto(
            input_data=operation,
            output_model=BankOperationRead
        )

    async def by_customer(
            self,
            search_data: BankOperationSearch
    ):

        operations = await self.operation_repo.get_by_customer_id(
            account_id=search_data.bank_account_id,
            customer_id=search_data.bank_customer_id
        )
        return self._list_adapter.validate_python(operations)

    async def by_date_interval(
            self,
            search_data: BankOperationSearch
    ):

        operations = await self.operation_repo.get_by_date_interval(
            account_id=search_data.bank_account_id,
            customer_id=search_data.bank_customer_id,
            start_date=search_data.since,
            end_date=search_data.till
        )
        return self._list_adapter.validate_python(operations)
