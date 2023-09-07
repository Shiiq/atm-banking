from fastapi import APIRouter, Depends

from app.application.dto import BankStatementInput, FullBankStatementInfo
from app.presentation.api.dependencies import get_provider

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(
        bank_statement_input: BankStatementInput,
        provider=Depends(get_provider)
) -> FullBankStatementInfo:

    handler = await provider.get_handler(
        key_class=bank_statement_input.operation_type
    )
    response = await handler.execute(bank_statement_input)
    return response
