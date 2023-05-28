from .account import BankAccountRead
from .customer import BankCustomerRead
from .operation import BankOperationRead
from ._base import DTO


class SummaryOperationInfo(DTO):

    account: BankAccountRead
    customer: BankCustomerRead
    operation: BankOperationRead

    class Config:
        allow_mutation = False
