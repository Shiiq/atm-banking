import logging
from pprint import PrettyPrinter

from src.infrastructure.config.db_config import get_db_config
# from src.infrastructure.config.db_config import get_db_config
from src.infrastructure.di.builder import build_container
from src.infrastructure.di.container import DIScope
from src.infrastructure.provider import build_provider, setup_handlers
from src.presentation.cli.app import CLIApp
from src.presentation.cli.handlers import InputHandler


async def cli_start():

    # logging.warning("setting up the application")
    # app = CLIApp(provider=provider,
    #              input_handler=input_handler,
    #              output_handler=output_handler)
    # container = build_container(db_config=get_db_config)
    db_config = get_db_config()
    container = build_container(db_config=db_config)
    # container = build_container(db_config=get_db_config)
    input_handler = InputHandler()
    output_handler = PrettyPrinter()

    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container, app_state=app_state)
        setup_handlers(provider=provider)

        logging.warning("setting up the application")
        app = CLIApp(
            provider=provider,
            input_handler=input_handler,
            output_handler=output_handler
        )
        logging.warning("running the cli application")
        await app.run()
