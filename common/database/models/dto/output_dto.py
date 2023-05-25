from .customer import BankCustomerRead
from .operation import BankOperationRead
from ._base import DTO


class SummaryOperationInfo(DTO):

    account: BankOperationRead
    customer: BankCustomerRead
    operation: BankOperationRead

    class Config:
        allow_mutation = False
