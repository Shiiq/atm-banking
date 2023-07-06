from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class DiMiddleware(BaseHTTPMiddleware):

    def __init__(
            self,
            app,
            container,
            scope_state
    ):
        super().__init__(app)
        self._container = container
        self._scope_state = scope_state

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example

        # process the request and get the response
        response = await call_next(request)
        return response