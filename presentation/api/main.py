from fastapi import FastAPI, Request

from .routers.bank_statement import bank_statement_router


app = FastAPI()
app.include_router(bank_statement_router)




async def run():
    app = FastAPI()
    pass