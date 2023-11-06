from contextlib import asynccontextmanager


from src.infrastructure.config.api_config import get_api_config
from src.infrastructure.config.db_config import get_db_config
from src.infrastructure.di.builder import build_container
from src.infrastructure.di.container import DIScope
from src.infrastructure.provider import build_provider, setup_handlers
from src.presentation.api.app import create_app, setup_app


@asynccontextmanager
async def lifespan(app):
    # container = build_container(db_config=get_db_config)
    db_config = get_db_config()
    container = build_container(db_config=db_config)
    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(
            di_container=container,
            app_state=app_state
        )
        setup_handlers(provider)
        setup_app(
            app=app,
            provider=provider
        )
        yield


app_config = get_api_config()
application = create_app(
    app_config=app_config,
    lifespan_callble=lifespan
)
