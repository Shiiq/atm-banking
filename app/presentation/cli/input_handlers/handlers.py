from app.application.dto import (BankOperationsFromInput,
                                 BankStatementInput,
                                 DepositInput,
                                 WithdrawInput)
from app.presentation.cli.common import ExitCommand, ExitOperation, WrongOperationError


class InputHandler:

    def parse(self, input_data: str) -> BankStatementInput | DepositInput | WithdrawInput:
        if input_data.strip().lower() == ExitCommand.EXIT:
            # TODO to fix EXC
            raise ExitOperation("Exiting")
        return self._parse(input_data)

    def _parse(self, input_data: str) -> BankStatementInput | DepositInput | WithdrawInput:
        operation, first_name, last_name, *args = input_data.strip().split()

        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            since = args[0]
            till = args[1]
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
            # TODO to fix EXC
            raise WrongOperationError("Wrong operation")
