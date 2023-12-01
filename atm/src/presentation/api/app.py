from contextlib import asynccontextmanager
from functools import partial

from fastapi import FastAPI
import uvicorn

from src.infrastructure.provider import Provider
from src.infrastructure.provider import build_provider
from src.infrastructure.provider import setup_provider
from src.infrastructure.database.db_config import DBConfig
from src.infrastructure.dependency_injection import DIScope
from src.infrastructure.dependency_injection import build_container
from src.presentation.api.dependencies import setup_dependencies
from src.presentation.api.exception_handlers import setup_exception_handlers
from src.presentation.api.routers import setup_routers
from .api_config import APIConfig


def setup_app(app: FastAPI, provider: Provider):
    """Setting up the app features."""

    setup_dependencies(app=app, provider=provider)
    setup_exception_handlers(app=app)
    setup_routers(app=app)


@asynccontextmanager
async def init_dependency_container_cm(app: FastAPI, **kwargs):
    """Initializing the dependency container."""

    db_config = kwargs["db_config"]
    container = build_container(db_config=db_config)
    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container, app_state=app_state)
        setup_provider(provider=provider)
        setup_app(app=app, provider=provider)
        yield


def create_app(api_config: APIConfig, db_config: DBConfig) -> FastAPI:
    """Create FastAPI application."""

    lifespan = partial(init_dependency_container_cm, db_config=db_config)
    app = FastAPI(
        debug=api_config.debug,
        title=api_config.title,
        lifespan=lifespan
    )
    return app


# def create_app(api_config: APIConfig) -> FastAPI:
#     app = FastAPI(
#         debug=api_config.debug,
#         title=api_config.title,
#     )
#     return app


async def run_app(app: FastAPI, api_config: APIConfig):
    """Running uvicorn web server."""

    server_config = uvicorn.Config(
        app=app,
        host=api_config.host,
        port=api_config.port
    )
    server = uvicorn.Server(config=server_config)
    await server.serve()
