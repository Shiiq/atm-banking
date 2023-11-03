import logging

from src.infrastructure.config.config_loader import Config
from src.infrastructure.config.db_config import DBConfig
from src.infrastructure.di import DIScope, build_container
from src.infrastructure.provider import build_provider, setup_handlers
from src.presentation.cli.app import CLIApp
from src.presentation.cli.handlers import InputHandler, OutputHandler


async def cli_start(config: Config):

    logging.warning("setting up the application cli")
    container = build_container(db_config=config.db)

    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container, app_state=app_state)
        input_handler = InputHandler()
        output_handler = OutputHandler()

        app = CLIApp.create_app(
            provider=provider,
            input_handler=input_handler,
            output_handler=output_handler
        )
        setup_handlers(provider=provider)

        logging.warning("setting up the application")
        app = CLIApp(
            provider=provider,
            input_handler=input_handler,
            output_handler=output_handler
        )
        logging.warning("running the cli application")
        await app.run()
