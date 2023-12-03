from atm.application.exceptions import ApplicationException
from atm.infrastructure.provider import Provider
from atm.presentation.cli.common.exceptions import CLIAppRuntimeError
from atm.presentation.cli.common.exceptions import ExitOperation
from atm.presentation.cli.common.exceptions import InputDataError
from atm.presentation.cli.common.exceptions import UnknownOperationError
from atm.presentation.cli.common.messages import REQUESTING_MSG
from atm.presentation.cli.common.messages import OPERATION_SUCCESS_MSG
from atm.presentation.cli.common.messages import WELCOME_MSG
from atm.presentation.cli.handlers import InputHandler, OutputHandler
from .base import CLIAppBase


class CLIApp(CLIAppBase):

    _RUNNING: bool
    _provider: Provider
    _input_handler: InputHandler
    _output_handler: OutputHandler

    async def run(self):
        if self._RUNNING:
            raise CLIAppRuntimeError
        else:
            await self._run()

    async def _run(self):

        self._RUNNING = True
        self._print(WELCOME_MSG)

        while self._RUNNING:
            input_data = input(REQUESTING_MSG)
            try:
                request = self._input_handler.parse(input_data)

            except ExitOperation as err:
                self._RUNNING = False
                self._print(err.ui_msg)
                continue

            except UnknownOperationError as err:
                self._print(err.ui_msg)
                continue

            except InputDataError as err:
                self._print(err.ui_msg)
                continue

            handler = await self._provider.get_handler(
                key=request.operation_type
            )
            try:
                response = await handler.execute(request)
                self._print(OPERATION_SUCCESS_MSG)
                self._print(response)

            except ApplicationException as err:
                self._print(err.ui_msg)

    def _print(self, msg):
        self._output_handler.print(msg)
