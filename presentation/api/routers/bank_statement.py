from fastapi import APIRouter, Depends

from application.usecases import BankStatement
from application.dto import BankStatementInput, BankOperationsInfo
from presentation.api.providers import Stub

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(
        bank_statement_input: BankStatementInput,
        handler=Depends(Stub(BankStatement))
) -> BankOperationsInfo:
    response = await handler.execute(bank_statement_input)
    return response
