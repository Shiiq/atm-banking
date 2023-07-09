from di import ScopeState
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from application.usecases import BaseUsecase
from infrastructure.di.container import DIContainer, DIScope


class DIMiddleware(BaseHTTPMiddleware):

    def __init__(
            self,
            app,
            container: DIContainer,
            scope_state: ScopeState,
            dependency: BaseUsecase
    ):
        super().__init__(app)
        self._container = container
        self._state = scope_state
        self._dependency = dependency

    async def dispatch(self, request: Request, call_next):
        async with self._container.enter_scope(
                scope=DIScope.REQUEST,
                state=self._state
        ) as request_state:
            base_usecase = await self._container.execute(
                required_dependency=self._dependency,
                scope=DIScope.REQUEST,
                state=self._state)
            request.state.base_usecase = base_usecase
            response = await call_next(request)
            return response
