from fastapi import FastAPI, Request

from infrastructure.config.db_config import get_db_config
from infrastructure.di.container import DIScope
from infrastructure.di.builder import build_container

from .routers.bank_statement import bank_statement_router


# app = FastAPI()


async def run():
    app = FastAPI()
    app.include_router(bank_statement_router)
    settings = get_db_config()
    container = build_container(db_config=settings)
    async with container.enter_scope(scope=DIScope.APP) as app_state:
        pass
