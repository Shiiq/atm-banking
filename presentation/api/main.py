import asyncio

from fastapi import FastAPI
import uvicorn

from application.usecases import BaseUsecase

from infrastructure.config.db_config import get_db_config
from infrastructure.di.container import DIScope
from infrastructure.di.builder import build_container
from infrastructure.mediator import Mediator

from presentation.api.middlewares import DIMiddleware
from presentation.api.providers import Stub
from presentation.api.routers import bank_statement_router


async def run():
    app = FastAPI()
    app.include_router(bank_statement_router)

    container = build_container(db_config=get_db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:

        mediator = Mediator(di_container=container,
                            app_state=app_state)

        app.dependency_overrides[Stub(Mediator)] = mediator.get_bank_statement_handler
        # app.add_middleware(DIMiddleware,
        #                    container=container,
        #                    app_state=app_state,
        #                    dependency=BaseUsecase)

        config = uvicorn.Config(app=app)
        server = uvicorn.Server(config)

        await server.serve()


if __name__ == "__main__":
    asyncio.run(run())
