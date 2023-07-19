import asyncio

import uvicorn
from fastapi import FastAPI

from application.operation_handlers import BankStatement, Deposit, Withdraw

from infrastructure.config.db_config import get_db_config
from infrastructure.di.container import DIScope
from infrastructure.di.builder import build_container
from infrastructure.provider import Provider

from presentation.api.exception_handlers import setup_exception_handlers
from presentation.api.routers import setup_routers


def create_app() -> FastAPI:
    app = FastAPI()
    return app

def setup_app(app: FastAPI):
    setup_routers(app)
    setup_exception_handlers(app)


async def run():
    app = FastAPI()

    setup_routers(app)
    setup_exception_handlers(app)

    container = build_container(db_config=get_db_config)

    async with container.enter_scope(scope=DIScope.APP) as app_state:

        provider = Provider(di_container=container,
                            app_state=app_state)

        app.dependency_overrides[BankStatement] = provider.get_bank_statement_handler
        app.dependency_overrides[Deposit] = provider.get_deposit_handler
        app.dependency_overrides[Withdraw] = provider.get_withdraw_handler

        # app.add_middleware(DIMiddleware,
        #                    container=container,
        #                    app_state=app_state,
        #                    dependency=BaseUsecase)

        config = uvicorn.Config(app=app)
        server = uvicorn.Server(config)

        await server.serve()


if __name__ == "__main__":
    asyncio.run(run())
