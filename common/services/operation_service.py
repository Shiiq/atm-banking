from common.database.models.db import *
from common.database.models.dto import BankOperationCreate, BankOperationRead
from common.unit_of_work import UnitOfWork

from ._base_service import BaseService


class OperationService(BaseService):

    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def operation_create(self, operation_data: BankOperationCreate) -> BankOperationRead:
        operation_orm = self._from_dto_to_orm(input_data=operation_data,
                                              output_model=BankOperationModel)
        operation = await self._uow.operation_repo.create(operation_orm)
        await self._uow.commit()
        return self._from_orm_to_dto(input_data=operation,
                                     output_model=BankOperationRead)

    async def operation_by_id(self, operation_id: int):
        operation = await self._uow.operation_repo.get_by_id(obj_id=operation_id)
        pass

    async def operations_by_customer(self, customer_id: int):
        operations = await self._uow.operation_repo.get_by_customer_id(customer_id=customer_id)
        pass

    async def operations_by_bank_account(self, bank_account_id: int):
        operations = await self._uow.operation_repo.get_by_bank_account_id(bank_account_id=bank_account_id)
        pass

    async def operations_by_date_interval(self, start_date, end_date):
        operations = await self._uow.operation_repo.get_by_date_interval(start_date=start_date,
                                                                         end_date=end_date)
        pass
