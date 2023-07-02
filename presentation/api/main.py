import di_analysis
from fastapi import FastAPI

from .routers.bank_statement import bank_statement_router


app = FastAPI()
app.include_router(bank_statement_router)


async def main():
    container = ...
