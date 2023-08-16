import uvicorn
from fastapi import FastAPI

from app.infrastructure.config.app_config import AppConfig
from app.infrastructure.provider import Provider

from app.presentation.api.exception_handlers import setup_exception_handlers
from app.presentation.api.providers import setup_dependencies
from app.presentation.api.routers import setup_routers


def create_app(app_config: AppConfig) -> FastAPI:
    app = FastAPI(debug=app_config.debug,
                  title=app_config.title)
    return app


def setup_app(app: FastAPI, provider: Provider):
    setup_dependencies(app, provider)
    setup_exception_handlers(app)
    setup_routers(app)


async def run_app(app: FastAPI, app_config: AppConfig):
    # logging prepare for launch api
    server_config = uvicorn.Config(app=app,
                                   host=app_config.host,
                                   port=app_config.port)
    server = uvicorn.Server(config=server_config)
    await server.serve()
