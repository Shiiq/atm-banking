from app.infrastructure.config.app_config import get_app_config
from app.infrastructure.config.db_config import get_db_config
from app.infrastructure.di.builder import build_container
from app.infrastructure.di.container import DIScope
from app.infrastructure.provider import build_provider, setup_api_handlers



async def main():

    app_config = get_app_config()

    container = build_container(db_config=get_db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:

        provider = build_provider(di_container=container,
                                  app_state=app_state)

        pass
