import re

from app.application.dto import (BankOperationsFromInput,
                                 BankStatementInput,
                                 DepositInput,
                                 WithdrawInput)
from app.presentation.cli.common import (ExitCommand,
                                         ExitOperation,
                                         InputDataError,
                                         ValidateDataError,
                                         WrongOperationError)

DEPOSIT_OR_WITHDRAW_PATTERN = r"(?P<operation_type>[deposit|withdraw]) (?P<first_name>[^\W\d]+) (?P<last_name>[^\W\d]+) (?P<amount>\d+)"


class InputHandler:

    def __init__(self):
        self.deposit_pattern = DEPOSIT_OR_WITHDRAW_PATTERN
        self.withdraw_pattern = DEPOSIT_OR_WITHDRAW_PATTERN

    def parse(self, input_data: str) -> BankStatementInput | DepositInput | WithdrawInput:
        if input_data.strip().lower() == ExitCommand.EXIT:
            raise ExitOperation("Exiting")
        return self.__parse(input_data)


    def __parse(self, input_data: str):
        print(input_data)
        match = re.match(self.deposit_pattern, input_data)
        print(match.groups) #("operation_type"))

        first_name = "john"
        last_name = "doe"
        amount = 700
        return DepositInput(first_name=first_name,
                            last_name=last_name,
                            amount=amount)

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
            raise WrongOperationError("Wrong operation")
