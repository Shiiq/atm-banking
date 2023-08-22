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
        pprint(response.model_dump(), indent=4)

    def print_error(self, error):
        pprint(error.msg, indent=4)

    async def _run(self):
        print(WELCOME_MESSAGE)
        while input_data := input(REQUESTING_MESSAGE):  # True

            try:
                request = self._input_handler.parse(input_data)
            except ExitOperation as err:
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

            handler = await self._provider.get_handler(
                key_class=request.operation_type
            )
            try:
                response = await handler.execute(request)
                self.print_result(response=response)
            except ApplicationException as err:
                print(err.msg)
                pass

    async def run(self):
        # logging prepare for launch cli
        await self._run()
