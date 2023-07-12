from infrastructure.database.models.db import BankOperationModel
from infrastructure.database.models.dto import (BankOperationCreate,
                                                BankOperationRead,
                                                BankOperationSearch)
from infrastructure.database.repositories import IOperationRepo
from .utils import DataConverter


class OperationService(DataConverter):

    def __init__(self, operation_repo: IOperationRepo):
        self.operation_repo = operation_repo

    async def create(self, create_data: BankOperationCreate) -> BankOperationRead:
        operation_orm = self._from_dto_to_orm(input_data=create_data,
                                              output_model=BankOperationModel)
        operation = await self.operation_repo.create(operation=operation_orm)
        return self._from_orm_to_dto(input_data=operation,
                                     output_model=BankOperationRead)

    async def by_id(self, search_data: BankOperationSearch) -> BankOperationRead:
        operation = await self.operation_repo.get_by_id(
            operation_id=search_data.id
        )
        return self._from_orm_to_dto(input_data=operation,
                                     output_model=BankOperationRead)

    async def by_account(self, search_data: BankOperationSearch):
        operations = await self.operation_repo.get_by_account_id(
            account_id=search_data.bank_account_id
        )
        return [
            self._from_orm_to_dto(input_data=operation, output_model=BankOperationRead)
            for operation in operations
        ]

    async def by_customer(self, search_data: BankOperationSearch):
        operations = await self.operation_repo.get_by_customer_id(
            customer_id=search_data.bank_customer_id
        )
        return [
            self._from_orm_to_dto(input_data=operation, output_model=BankOperationRead)
            for operation in operations
        ]

    async def by_date_interval(self, search_data: BankOperationSearch):
        operations = await self.operation_repo.get_by_date_interval(
            account_id=search_data.bank_account_id,
            customer_id=search_data.bank_customer_id,
            start_date=search_data.since,
            end_date=search_data.till
        )
        return [
            self._from_orm_to_dto(input_data=operation, output_model=BankOperationRead)
            for operation in operations
        ]
