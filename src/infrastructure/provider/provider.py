from typing import Generic, TypeVar, Dict

from di import ScopeState

from src.infrastructure.di import DIContainer, DIScope

HandlerTypeT = TypeVar("HandlerTypeT")
HandlerImplT = TypeVar("HandlerImplT")


class Provider(Generic[HandlerTypeT, HandlerImplT]):

    _handlers: Dict[HandlerTypeT, HandlerImplT]

    def __init__(self, di_container: DIContainer, app_state: ScopeState):
        self._app_state = app_state
        self._di_container = di_container
        self._handlers = {}

    async def get_handler(self, key: HandlerTypeT) -> HandlerImplT:
        handler = self._handlers.get(key)
        return await self._build_handler(handler)

    def register_handler(self, key: HandlerTypeT, handler: HandlerImplT):
        self._handlers[key] = handler

    async def _build_handler(self, handler: HandlerImplT) -> HandlerImplT:
        async with self._di_container.enter_scope(
                scope=DIScope.REQUEST, state=self._app_state
        ) as request_state:
            handler = await self._di_container.execute(
                required_dependency=handler,
                scope=DIScope.REQUEST,
                state=request_state
            )
            return handler
