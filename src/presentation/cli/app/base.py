from typing import Generic, TypeVar

ProviderT = TypeVar("ProviderT")
InputHandlerT = TypeVar("InputHandlerT")
OutputHandlerT = TypeVar("OutputHandlerT")


class CLIAppBase(Generic[ProviderT, InputHandlerT, OutputHandlerT]):

    _RUNNING: bool
    _provider: ProviderT
    _input_handler: InputHandlerT
    _output_handler: OutputHandlerT

    def __init__(
            self,
            provider: ProviderT,
            input_handler: InputHandlerT,
            output_handler: OutputHandlerT
    ):
        self._RUNNING = False
        self._provider = provider
        self._input_handler = input_handler
        self._output_handler = output_handler

    @classmethod
    def create_app(cls, provider, input_handler, output_handler):
        return cls(
            provider=provider,
            input_handler=input_handler,
            output_handler=output_handler
        )
