import logging

from src.infrastructure.config.config_loader import Config
from src.infrastructure.di import DIScope, build_container
from src.infrastructure.provider import build_provider, setup_provider
from src.presentation.cli.app import CLIApp
from src.presentation.cli.handlers import InputHandler, OutputHandler


async def cli_start(config: Config):

    logging.warning("setting up the application cli")
    container = build_container(db_config=config.db)

    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container, app_state=app_state)
        setup_provider(provider=provider)
        app = CLIApp.create_app(
            provider=provider,
            input_handler=InputHandler(),
            output_handler=OutputHandler()
        )
        logging.warning("running the cli application")
        await app.run()
