import logging

from atm_banking.infrastructure.config import Config
from atm_banking.infrastructure.dependency_injection import DIScope
from atm_banking.infrastructure.dependency_injection import build_container
from atm_banking.infrastructure.provider import build_provider, setup_provider
from atm_banking.presentation.api.app import create_app, setup_app, run_app


# async def api_start(config: Config):
#
#     logging.warning("setting up the application api")
#     app = create_app(app_config=config.api)
#     container = build_container(db_config=config.db)
#
#     async with container.enter_scope(scope=DIScope.APP) as app_state:
#         provider = build_provider(di_container=container, app_state=app_state)
#         setup_provider(provider=provider)
#         setup_app(app=app, provider=provider)
#         logging.warning("running the application api")
#         await run_app(app=app, app_config=config.api)


async def api_start(config: Config):

    logging.warning("setting up the application api")
    app = create_app(api_config=config.api, db_config=config.db)
    logging.warning("running the application api")
    await run_app(app=app, api_config=config.api)
