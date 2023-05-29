from datetime import date, datetime

from application.services import (AccountService,
                                  CustomerService,
                                  OperationService)
from infrastructure.database.models import dto
from infrastructure.unit_of_work import UnitOfWork


class BankStatement:

    # TODO redesign
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)

    async def __call__(self, input_data: dto.BankStatementInput) -> dto.BankOperationsInfo:
        customer = await self._get_customer(
            customer_data=input_data.customer
        )
        operations = await self._get_operations(
            operations_data=dto.BankOperationSearch(bank_customer_id=customer.id,
                                                    bank_account_id=customer.bank_account_id,
                                                    since=input_data.operation.since,
                                                    till=input_data.operation.till)
        )

    async def _get_customer(self, customer_data: dto.CustomerInput) -> dto.BankCustomerRead:
        try:
            customer = await self._customer_service.customer_by_fullname(
                customer_search_data=dto.BankCustomerSearch(first_name=customer_data.first_name,
                                                            last_name=customer_data.last_name)
            )
            return customer
        # TODO custom exceptions
        except ValueError:
            pass

    def _check_dates(self, start_date: datetime, end_date: datetime):
        return start_date >= end_date

    async def _get_operations(self, operations_data: dto.BankOperationSearch):
        if not self._check_dates(start_date=operations_data.since,
                                 end_date=operations_data.till):
            # TODO custom exceptions
            raise ValueError
        operations = await self._operation_service.operations_by_date_interval(operation_search_data=operations_data)
        pass
