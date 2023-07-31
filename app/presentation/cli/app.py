from app.application.dto import BankStatementInput, DepositInput, WithdrawInput
from app.application.operation_handlers import BankStatement, Deposit, Withdraw
from app.infrastructure.provider import Provider
from app.presentation.cli.common import (EXIT_MESSAGE,
                                         RETRY_MESSAGE,
                                         REQUESTING_MESSAGE,
                                         WELCOME_MESSAGE,
                                         ExitOperation,
                                         WrongOperationError)
from app.presentation.cli.handlers import ExceptionHandler, InputHandler


class CLIApp:

    def __init__(self):
        self._exception_handler: ExceptionHandler = ...
        self._input_handler: InputHandler = ...
        self._provider: Provider = ...
        self.handlers = {}

    async def get_handler(self, operation):
        return await self._provider.get_handler(operation)

    def _run(self):
        print(WELCOME_MESSAGE)
        while True:
            try:
                input_data = input(REQUESTING_MESSAGE)
                request = self._input_handler.parse(input_data)
            except ExitOperation as e:
                # logging exiting
                print(EXIT_MESSAGE)
                self._exception_handler.handle(e)
                break
            except WrongOperationError as e:
                # logging wrong operation
                print(RETRY_MESSAGE)
                self._exception_handler.handle(e)
                continue
            # operation_handler = self.get_handler[request.operation_type]
            # process

    def run(self):
        # logging prepare for launch cli
        self._run()
