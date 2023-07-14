import asyncio

from fastapi import FastAPI
import uvicorn

from application.usecases import BankStatement, Deposit, Withdraw, IUsecase

from infrastructure.config.db_config import get_db_config
from infrastructure.di.container import DIScope
from infrastructure.di.builder import build_container
from infrastructure.provider import Provider

# from presentation.api.middlewares import DIMiddleware
from presentation.api.providers import Stub
from presentation.api.routers import (
    bank_statement_router,
    # deposit_router,
    additional_router
)


async def run():
    app = FastAPI()
    app.include_router(additional_router)

    app.include_router(bank_statement_router)
    # app.include_router(deposit_router)

    container = build_container(db_config=get_db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:

        provider = Provider(di_container=container,
                            app_state=app_state)

        app.dependency_overrides[Stub(BankStatement)] = provider.get_bank_statement_handler
        # app.dependency_overrides[Deposit] = provider.get_deposit_handler
        # app.dependency_overrides[]

        # app.add_middleware(DIMiddleware,
        #                    container=container,
        #                    app_state=app_state,
        #                    dependency=BaseUsecase)

        config = uvicorn.Config(app=app)
        server = uvicorn.Server(config)

        await server.serve()


if __name__ == "__main__":
    asyncio.run(run())
