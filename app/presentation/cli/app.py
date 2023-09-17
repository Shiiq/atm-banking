import logging
from pprint import PrettyPrinter

from app.application.exceptions import ApplicationException
from app.infrastructure.provider import Provider

from app.presentation.cli.common.exceptions import (ExitOperation,
                                                    InputDataError,
                                                    WrongOperationError)
from app.presentation.cli.common.messages import (REQUESTING_MESSAGE,
                                                  OPERATION_SUCCESS_MESSAGE,
                                                  WELCOME_MESSAGE)
from app.presentation.cli.handlers import InputHandler

_logger = logging.getLogger(__name__)


class CLIApp:

    _RUNNING: bool

    def __init__(
            self,
            provider: Provider,
            input_handler: InputHandler,
            output_handler: PrettyPrinter
    ):
        self._provider = provider
        self._input_handler = input_handler
        self._output_handler = output_handler
        self._RUNNING = False

    async def run(self):
        await self._run()

    def _print_result(self, msg):
        self._output_handler.pprint(msg)

    async def _run(self):
        self._RUNNING = True
        print(WELCOME_MESSAGE)
        while self._RUNNING:
            input_data = input(REQUESTING_MESSAGE)
            try:
                request = self._input_handler.parse(input_data)
            except ExitOperation as err:
                self._RUNNING = False
                _logger.info(
                    "Received the 'EXIT' command, work with the terminal is done."
                )
                print(err.ui_msg)
                continue
            except WrongOperationError as err:
                _logger.info("Received unknown operation")
                print(err.ui_msg)
                continue
            except InputDataError as err:
                _logger.info("Received incorrect data")
                print(err.ui_msg)
                continue

            handler = await self._provider.get_handler(
                key_class=request.operation_type
            )
            try:
                response = await handler.execute(request)
                response = response.model_dump(exclude_none=True)
                print(OPERATION_SUCCESS_MESSAGE)
                self._print_result(msg=response)
            except ApplicationException as err:
                self._print_result(msg=err.msg)
                continue
