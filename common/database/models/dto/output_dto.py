from typing import Optional

from .customer import BankCustomerRead
from .operation import BankOperationRead
from ._base import DTO


class SummaryOperationInfo(DTO):

    customer: Optional[BankCustomerRead]
    operation: Optional[BankOperationRead]
