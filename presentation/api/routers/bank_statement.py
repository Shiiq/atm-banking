from fastapi import APIRouter

from infrastructure.database.models.dto import BankStatementInput, BankOperationSearch

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(bank_statement_input: BankStatementInput):
    bos = BankOperationSearch(since=bank_statement_input.since,
                              till=bank_statement_input.till)
    print(bos.since.date())
    return bank_statement_input
