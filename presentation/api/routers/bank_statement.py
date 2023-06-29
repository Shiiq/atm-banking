from fastapi import APIRouter

from infrastructure.database.models.dto import BankStatementInput

bank_statement_router = APIRouter(
    # prefix="/bank_statement"
)


@bank_statement_router.post(path="/")
async def bank_statement(bank_statement_input: BankStatementInput):
    # sess = ...
    # uow = ... (sess)
    print(bank_statement_input)
    return bank_statement_input
