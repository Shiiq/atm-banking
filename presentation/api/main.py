from fastapi import FastAPI, Request

from .routers.bank_statement import bank_statement_router


app = FastAPI()
app.include_router(bank_statement_router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request.state.temp = "asdasd"
    response = await call_next(request)
    return response
