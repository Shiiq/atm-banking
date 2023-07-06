from fastapi import APIRouter, Request

from infrastructure.database.models.dto import BankStatementInput, BankOperationSearch

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(bank_statement_input: BankStatementInput, request: Request):
    bos = BankOperationSearch(since=bank_statement_input.since,
                              till=bank_statement_input.till)
    print(type(bank_statement_input))
    print(request.state.temp)
    return bank_statement_input
