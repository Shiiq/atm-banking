import logging
from pprint import PrettyPrinter

from app.infrastructure.config.db_config import get_db_config
from app.infrastructure.di.builder import build_container
from app.infrastructure.di.container import DIScope
from app.infrastructure.provider import build_provider, setup_handlers
from app.presentation.cli.app import CLIApp
from app.presentation.cli.handlers import InputHandler


async def cli_start():

    # input_handler = InputHandler()
    # output_handler = PrettyPrinter()
    # logging.warning("setting up the application")
    # app = CLIApp(provider=provider,
    #              input_handler=input_handler,
    #              output_handler=output_handler)
    container = build_container(db_config=get_db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:
        provider = build_provider(di_container=container,
                                  app_state=app_state)
        setup_handlers(provider=provider)
        input_handler = InputHandler()
        output_handler = PrettyPrinter()
        logging.warning("setting up the application")
        app = CLIApp(provider=provider,
                     input_handler=input_handler,
                     output_handler=output_handler)
        logging.warning("running the cli application")
        await app.run()
