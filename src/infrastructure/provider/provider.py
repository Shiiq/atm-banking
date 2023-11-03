from di import ScopeState

from src.infrastructure.di import DIContainer, DIScope


class Provider:

    def __init__(self, di_container: DIContainer, app_state: ScopeState):
        self._app_state = app_state
        self._di_container = di_container
        self._handlers = {}

    async def get_handler(self, key_class):

        handler = self._handlers.get(key_class)
        return await self._build_handler(handler)

    def register_handler(self, key_class, handler_class):

        self._handlers[key_class] = handler_class

    async def _build_handler(self, handler_class):

        async with self._di_container.enter_scope(
                scope=DIScope.REQUEST, state=self._app_state
        ) as request_state:
            handler = await self._di_container.execute(
                required_dependency=handler_class,
                scope=DIScope.REQUEST,
                state=request_state
            )
            return handler
