from fastapi import FastAPI

from .bank_statement import bank_statement_router
from .deposit import deposit_router
from .withdraw import withdraw_router


def setup_routers(app: FastAPI):
    app.include_router(bank_statement_router)
    app.include_router(deposit_router)
    app.include_router(withdraw_router)
