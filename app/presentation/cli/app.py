from app.application.dto import (BankStatementInput,
                                 DepositInput,
                                 WithdrawInput)
from app.infrastructure.provider import Provider
from app.presentation.cli.common import (EXIT_MESSAGE,
                                         RETRY_MESSAGE,
                                         REQUESTING_MESSAGE,
                                         WELCOME_MESSAGE,
                                         ExitOperation,
                                         WrongOperationError)
from app.presentation.cli.input_handlers import InputHandler


class CLIApp:

    def __init__(self):
        self._input_handler: InputHandler = ...
        self._provider: Provider = ...

    def register_handler(self):
        pass

    def run(self):
        # logging prepare for launch cli
        print(WELCOME_MESSAGE)
        while True:
            try:
                request = input(REQUESTING_MESSAGE)
            except ExitOperation:
                # logging exiting
                print(EXIT_MESSAGE)
                break
            except WrongOperationError:
                # logging wrong operation
                print(RETRY_MESSAGE)
                continue
            # operation_handler = self.get_handler[operation_handler.operation_type]
            # process
