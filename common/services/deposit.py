from common.uow import UnitOfWork


class DepositOperationService:

    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    pass
