from application.services import (AccountService,
                                  CustomerService,
                                  OperationService)
from infrastructure.unit_of_work import UnitOfWork


class BaseUsecase:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)
