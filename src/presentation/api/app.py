import uvicorn
from fastapi import FastAPI

from src.infrastructure.config.api_config import AppConfig
from src.infrastructure.provider import Provider

from src.presentation.api.exception_handlers import setup_exception_handlers
from src.presentation.api.dependencies import setup_dependencies
from src.presentation.api.routers import setup_routers


def create_app(app_config: AppConfig) -> FastAPI:
    app = FastAPI(debug=app_config.debug,
                  title=app_config.title)
    return app


def setup_app(app: FastAPI, provider: Provider):
    setup_dependencies(app, provider)
    setup_exception_handlers(app)
    setup_routers(app)


async def run_app(app: FastAPI, app_config: AppConfig):
    server_config = uvicorn.Config(app=app,
                                   host=app_config.host,
                                   port=app_config.port)
    server = uvicorn.Server(config=server_config)
    await server.serve()
