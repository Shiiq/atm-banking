from common.database.models.constants import BankOperationsFromInput
from common.database.models.db import *
from common.database.models.dto import *


class InputParserService:

    # input data examples
    # "withdraw jake james 100500"
    # "deposit jake james 7000"
    # "bank_statement jake james 2023-01-01 2023-05-01"

    @staticmethod
    def parse_input(input_data: str) -> BankStatementInput | DepositInput | WithdrawInput:
        operation, first_name, last_name, *args = input_data.strip().split()
        customer = CustomerInput(first_name=first_name, last_name=last_name)

        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            since, till = args[0], args[1]
            operation = OperationInput(since=since, till=till)
            return BankStatementInput(customer=customer, operation=operation)

        elif operation.lower() == BankOperationsFromInput.DEPOSIT:
            amount = args[0]
            operation = OperationInput(amount=amount)
            return DepositInput(customer=customer, operation=operation)

        elif operation.lower() == BankOperationsFromInput.WITHDRAW:
            amount = args[0]
            operation = OperationInput(amount=amount)
            return WithdrawInput(customer=customer, operation=operation)

        else:
            # TODO to fix
            raise Exception("Wrong operation")
