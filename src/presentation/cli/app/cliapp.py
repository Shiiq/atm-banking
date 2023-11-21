import logging

from src.application.exceptions import ApplicationException
from src.infrastructure.provider import Provider
from src.presentation.cli.common.exceptions import ExitOperation
from src.presentation.cli.common.exceptions import InputDataError
from src.presentation.cli.common.exceptions import WrongOperationError
from src.presentation.cli.common.messages import REQUESTING_MESSAGE
from src.presentation.cli.common.messages import OPERATION_SUCCESS_MESSAGE
from src.presentation.cli.common.messages import WELCOME_MESSAGE
from src.presentation.cli.handlers import InputHandler, OutputHandler
from .base import CLIAppBase

_logger = logging.getLogger(__name__)


class CLIApp(CLIAppBase):

    _RUNNING: bool
    _provider: Provider
    _input_handler: InputHandler
    _output_handler: OutputHandler

    async def run(self):
        # runs the main loop for application cli
        if not self._RUNNING:
            await self._run()
        else:
            # TODO raise
            pass

    def _print(self, msg):
        self._output_handler.print(msg)

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
                key=request.operation_type
            )
            try:
                response = await handler.execute(request)
                # response = response.model_dump(exclude_none=True)
                print(OPERATION_SUCCESS_MESSAGE)
                self._print(response)
            except ApplicationException as err:
                self._print(err)
            continue
