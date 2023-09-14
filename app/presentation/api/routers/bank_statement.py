from fastapi import APIRouter, Depends
from starlette import status

from app.application.dto import BankStatementInput, ShortBankStatementInfo
from app.presentation.api.dependencies import get_provider

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(
    path="/",
    response_model=ShortBankStatementInfo,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
async def bank_statement(
        bank_statement_input: BankStatementInput,
        provider=Depends(get_provider)
) -> ShortBankStatementInfo:

    handler = await provider.get_handler(
        key_class=bank_statement_input.operation_type
    )
    response = await handler.execute(bank_statement_input)
    return response
