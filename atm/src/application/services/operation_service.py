from datetime import date, datetime, time
from uuid import UUID

from pydantic import TypeAdapter

from src.application.dto import BankOperationCreate
from src.application.dto import BankOperationRead
from src.application.dto import OperationShortResponse
from src.application.interfaces import IOperationRepo
from src.infrastructure.database.models import BankOperationModel
from .data_converter import DataConverterMixin


class OperationService(DataConverterMixin):

    def __init__(self, operation_repo: IOperationRepo):
        self.operation_repo = operation_repo
        self.list_adapter = TypeAdapter(list[OperationShortResponse])

    async def create(
            self,
            create_data: BankOperationCreate
    ) -> BankOperationRead:

        operation_orm = self.from_dto_to_orm(
            input_data=create_data,
            output_model=BankOperationModel
        )
        operation = await self.operation_repo.create(operation=operation_orm)
        return self.from_orm_to_dto(
            input_data=operation,
            output_model=BankOperationRead
        )

    async def get_by_date_interval(
            self,
            account_id: UUID,
            customer_id: UUID,
            since: date,
            till: date
    ) -> list[OperationShortResponse]:

        start_date = datetime.combine(
            since,
            time(hour=0, minute=0, second=0, microsecond=0)
        )
        end_date = datetime.combine(
            till,
            time(hour=23, minute=59, second=59, microsecond=999999)
        )
        operations = await self.operation_repo.get_by_date_interval(
            account_id=account_id,
            customer_id=customer_id,
            start_date=start_date,
            end_date=end_date
        )
        return self.list_adapter.validate_python(operations)
