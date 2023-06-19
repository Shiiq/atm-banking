from datetime import datetime

from infrastructure.database.models.constants import BankOperationsFromInput
from infrastructure.database.models.dto import (CustomerInput,
                                                OperationInput,
                                                BankStatementInput,
                                                DepositInput,
                                                WithdrawInput)

FORMAT = "%d/%m/%Y"


class InputParserService:

    # @staticmethod
    def parse(self, input_data: str) -> BankStatementInput | DepositInput | WithdrawInput:
        operation, first_name, last_name, *args = input_data.strip().split()
        customer = CustomerInput(first_name=first_name, last_name=last_name)

        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            since = datetime.strptime(args[0], FORMAT)
            till = datetime.strptime(args[1], FORMAT)
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
            raise ValueError("Wrong operation")
