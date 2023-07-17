from application.services import (AccountService,
                                  CustomerService,
                                  OperationService)
from infrastructure.unit_of_work import UnitOfWork


# class BaseUsecase:
#
#     def __init__(self, uow: UnitOfWork):
#         self.uow = uow
#         self._account_service = AccountService(uow=uow)
#         self._customer_service = CustomerService(uow=uow)
#         self._operation_service = OperationService(uow=uow)


class IUsecase:

    def __init__(
            self,
            uow: UnitOfWork,
            account_service: AccountService,
            customer_service: CustomerService,
            operation_service: OperationService
    ):
        print("IUSECASE INIT")
        self._uow = uow
        self._account_service = account_service
        self._customer_service = customer_service
        self._operation_service = operation_service
