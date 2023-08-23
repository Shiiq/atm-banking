from app.infrastructure.config.db_config import get_db_config
from app.infrastructure.di.builder import build_container
from app.infrastructure.di.container import DIScope
from app.infrastructure.provider import build_provider, setup_handlers
from app.presentation.cli.app import CLIApp
from app.presentation.cli.handlers import InputHandler


async def cli_start():
    print(__name__)
    container = build_container(db_config=get_db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:

        provider = build_provider(di_container=container,
                                  app_state=app_state)
        setup_handlers(provider=provider)
        input_handler = InputHandler()

        app = CLIApp(provider=provider,
                     input_handler=input_handler)
        await app.run()
