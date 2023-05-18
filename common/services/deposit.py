from common.services.alt_customer import AltCustomerService
from common.uow import UnitOfWork


class DepositUseCase:

    def __init__(self, uow: UnitOfWork, customer_service: AltCustomerService):
        self._uow = uow
        self._customer_service = customer_service


    pass
