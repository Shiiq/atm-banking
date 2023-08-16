from pprint import pprint

from app.application.exceptions import ApplicationException
from app.infrastructure.provider import Provider

from app.presentation.cli.common.exceptions import (ExitOperation,
                                                    InputDataError,
                                                    WrongOperationError)
from app.presentation.cli.common.messages import (EXIT_MESSAGE,
                                                  INCORRECT_DATA_MESSAGE,
                                                  REQUESTING_MESSAGE,
                                                  WELCOME_MESSAGE,
                                                  WRONG_OPERATION_MESSAGE)
from app.presentation.cli.handlers import ExceptionHandler, InputHandler


class CLIApp:

    def __init__(
            self,
            provider: Provider,
            input_handler: InputHandler
    ):
        #self._exception_handler: ExceptionHandler = ...
        self._input_handler = input_handler
        self._provider = provider

    def print_result(self, response):
        pprint(response.model_dump())

    def print_error(self, error):
        pprint(error.msg)

    async def _get_handler(self, operation):
        return await self._provider.get_handler(operation)

    async def _run(self):
        print(WELCOME_MESSAGE)
        while True:
            try:
                input_data = input(REQUESTING_MESSAGE)
                request = self._input_handler.parse(input_data)
            except ExitOperation:
                # logging exiting
                print(EXIT_MESSAGE)
                break
            except WrongOperationError as err:
                # logging wrong operation
                print(WRONG_OPERATION_MESSAGE)
                continue
            except InputDataError as err:
                print(INCORRECT_DATA_MESSAGE)
                continue
            operation_handler = await self._get_handler(
                operation=request.operation_type
            )
            try:
                response = await operation_handler.execute(request)
                self.print_result(response=response)
            except ApplicationException as err:
                pass

    async def run(self):
        # logging prepare for launch cli
        await self._run()
