import logging

from src.infrastructure.config.config_loader import Config
from src.infrastructure.config.api_config import get_api_config
from src.infrastructure.config.db_config import get_db_config
from src.infrastructure.di.builder import build_container
from src.infrastructure.di.container import DIScope
from src.infrastructure.provider import build_provider, setup_handlers
from src.presentation.api.app import create_app, setup_app, run_app


async def api_start(config: Config):

    app_config = config.api
    db_config = config.db
    logging.warning("setting up the application")
    app = create_app(app_config=app_config)
    # container = build_container(db_config=get_db_config)
    db_config = get_db_config()
    container = build_container(db_config=db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container, app_state=app_state)
        setup_handlers(provider=provider)
        setup_app(app=app, provider=provider)
        logging.warning("running the api application")
        await run_app(app=app, app_config=app_config)
