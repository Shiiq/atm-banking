from fastapi import APIRouter, Depends

from application.dto import BankStatementInput, BankOperationsInfo
from application.operation_handlers import BankStatement
from presentation.api.providers import Stub

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(
        bank_statement_input: BankStatementInput,
        handler=Depends(Stub(BankStatement))
) -> BankOperationsInfo:
    response = await handler.execute(bank_statement_input)
    return response
