from di import ScopeState
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.infrastructure.di.container import DIContainer, DIScope


class DIMiddleware(BaseHTTPMiddleware):

    def __init__(
            self,
            app,
            container: DIContainer,
            app_state: ScopeState,
            dependency
    ):
        super().__init__(app)
        self.container = container
        self.app_state = app_state
        self.dependency = dependency

    async def dispatch(self, request: Request, call_next):
        async with self.container.enter_scope(
                scope=DIScope.REQUEST,
                state=self.app_state
        ) as request_state:
            base_usecase = await self.container.execute(
                required_dependency=self.dependency,
                scope=DIScope.REQUEST,
                state=request_state
            )
            request.state.base_usecase = base_usecase
            response = await call_next(request)
            return response
