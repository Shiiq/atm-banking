from src.application.services import AccountService
from src.application.services import CustomerService
from src.application.services import OperationService
from src.application.interfaces import IUnitOfWork


class BaseHandler:

    def __init__(
            self,
            uow: IUnitOfWork,
            account_service: AccountService,
            customer_service: CustomerService,
            operation_service: OperationService
    ):
        self._uow = uow
        self._account_service = account_service
        self._customer_service = customer_service
        self._operation_service = operation_service
