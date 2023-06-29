from datetime import datetime

from infrastructure.database.models.constants import BankOperationsFromInput
from infrastructure.database.models.dto import (BankStatementInput,
                                                DepositInput,
                                                WithdrawInput)

FORMAT = "%d/%m/%Y"


class InputParserService:

    # @staticmethod
    def parse(self, input_data: str) -> BankStatementInput | DepositInput | WithdrawInput:
        operation, first_name, last_name, *args = input_data.strip().split()

        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            since = datetime.strptime(args[0], FORMAT)
            till = datetime.strptime(args[1], FORMAT)
            return BankStatementInput(first_name=first_name,
                                      last_name=last_name,
                                      since=since,
                                      till=till)

        elif operation.lower() == BankOperationsFromInput.DEPOSIT:
            amount = args[0]
            return DepositInput(first_name=first_name,
                                last_name=last_name,
                                amount=amount)

        elif operation.lower() == BankOperationsFromInput.WITHDRAW:
            amount = args[0]
            return WithdrawInput(first_name=first_name,
                                 last_name=last_name,
                                 amount=amount)
        else:
            # TODO to fix
            raise ValueError("Wrong operation")
