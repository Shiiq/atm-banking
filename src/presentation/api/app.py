import uvicorn
from fastapi import FastAPI

from src.infrastructure.provider import Provider
from src.presentation.api.dependencies import setup_dependencies
from src.presentation.api.exception_handlers import setup_exception_handlers
from src.presentation.api.routers import setup_routers
from .api_config import APIConfig


def create_app(app_config: APIConfig) -> FastAPI:
    app = FastAPI(debug=app_config.debug, title=app_config.title)
    return app


def setup_app(app: FastAPI, provider: Provider):
    setup_dependencies(app=app, provider=provider)
    setup_exception_handlers(app=app)
    setup_routers(app=app)


async def run_app(app: FastAPI, app_config: APIConfig):
    server_config = uvicorn.Config(
        app=app,
        host=app_config.host,
        port=app_config.port
    )
    server = uvicorn.Server(config=server_config)
    await server.serve()
