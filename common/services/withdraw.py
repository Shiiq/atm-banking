from common.uow import UnitOfWork


class WithdrawOperationService:

    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    pass
