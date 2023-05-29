from infrastructure.database.models.db import BankOperationModel
from infrastructure.database.models.dto import (BankOperationCreate,
                                                BankOperationRead,
                                                BankOperationSearch)
from ._base_service import BaseService


class OperationService(BaseService):

    async def operation_create(self, operation_data: BankOperationCreate) -> BankOperationRead:
        operation_orm = self._from_dto_to_orm(input_data=operation_data,
                                              output_model=BankOperationModel)
        operation = await self._uow.operation_repo.create(operation_orm)
        return self._from_orm_to_dto(input_data=operation,
                                     output_model=BankOperationRead)

    async def operation_by_id(self, operation_search_data: BankOperationSearch) -> BankOperationRead:
        operation = await self._uow.operation_repo.get_by_id(
            obj_id=operation_search_data.id
        )
        return self._from_orm_to_dto(input_data=operation,
                                     output_model=BankOperationRead)

    async def operations_by_customer(self, operation_search_data: BankOperationSearch):
        operations = await self._uow.operation_repo.get_by_customer_id(
            customer_id=operation_search_data.bank_customer_id
        )
        return [
            self._from_orm_to_dto(input_data=operation, output_model=BankOperationRead)
            for operation in operations
        ]

    async def operations_by_bank_account(self, operation_search_data: BankOperationSearch):
        operations = await self._uow.operation_repo.get_by_bank_account_id(
            bank_account_id=operation_search_data.bank_account_id)
        return [
            self._from_orm_to_dto(input_data=operation, output_model=BankOperationRead)
            for operation in operations
        ]

    async def operations_by_date_interval(self, operation_search_data: BankOperationSearch):
        operations = await self._uow.operation_repo.get_by_date_interval(
            customer_id=operation_search_data.bank_customer_id,
            bank_account_id=operation_search_data.bank_account_id,
            start_date=operation_search_data.since,
            end_date=operation_search_data.till
        )
        return [
            self._from_orm_to_dto(input_data=operation, output_model=BankOperationRead)
            for operation in operations
        ]

    async def operation_update(self):
        pass

    async def operation_delete(self):
        pass
