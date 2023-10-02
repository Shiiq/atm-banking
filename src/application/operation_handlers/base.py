from src.application.services import (AccountService,
                                      CustomerService,
                                      OperationService)
from src.infrastructure.unit_of_work import UnitOfWork


class BaseHandler:

    def __init__(
            self,
            uow: UnitOfWork,
            account_service: AccountService,
            customer_service: CustomerService,
            operation_service: OperationService
    ):
        self._uow = uow
        self._account_service = account_service
        self._customer_service = customer_service
        self._operation_service = operation_service