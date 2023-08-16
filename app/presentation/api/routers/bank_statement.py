from fastapi import APIRouter, Depends

from app.application.dto import BankStatementInput, BankOperationsInfo
from app.application.operation_handlers import BankStatement
from app.presentation.api.providers import Stub

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(
        bank_statement_input: BankStatementInput,
        handler=Depends(Stub(BankStatement))
) -> BankOperationsInfo:
    print("ENTERING BANK_STATEMENT PATH OPERATION")
    print(type(handler), handler)
    handler = await handler
    response = await handler.execute(bank_statement_input)
    return response
