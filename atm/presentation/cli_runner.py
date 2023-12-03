import logging

from atm.infrastructure.config import Config
from atm.infrastructure.dependency_injection import DIScope
from atm.infrastructure.dependency_injection import build_container
from atm.infrastructure.provider import build_provider, setup_provider
from atm.presentation.cli.app import CLIApp
from atm.presentation.cli.handlers import InputHandler, OutputHandler


async def cli_start(config: Config):

    logging.warning("setting up the application cli")
    container = build_container(db_config=config.db)

    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container, app_state=app_state)
        setup_provider(provider=provider)
        app = CLIApp.create(
            provider=provider,
            input_handler=InputHandler(),
            output_handler=OutputHandler()
        )
        logging.warning("running the application cli")
        await app.run()
