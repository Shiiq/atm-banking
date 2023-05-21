from common.unit_of_work import UnitOfWork
from ._base_service import BaseService


class OperationService(BaseService):

    def __init__(self, uow: UnitOfWork):
        self._uow = uow
