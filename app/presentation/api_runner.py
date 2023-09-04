import logging

from app.infrastructure.config.app_config import get_app_config
from app.infrastructure.config.db_config import get_db_config
from app.infrastructure.di.builder import build_container
from app.infrastructure.di.container import DIScope
from app.infrastructure.provider import build_provider, setup_handlers
from app.presentation.api.app import create_app, setup_app, run_app


async def api_start():

    app_config = get_app_config()
    logging.warning("setting up the application")
    app = create_app(app_config=app_config)
    container = build_container(db_config=get_db_config)
    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container,
                                  app_state=app_state)
        setup_handlers(provider=provider)
        setup_app(app=app, provider=provider)
        logging.warning("running the api application")
        await run_app(app=app, app_config=app_config)
