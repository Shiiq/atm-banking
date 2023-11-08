from fastapi import APIRouter, Depends
from starlette import status

from src.application.dto import BankStatementRequest, BankStatementShortResponse
from src.presentation.api.dependencies import get_provider

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(
    path="/",
    response_model=BankStatementShortResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
async def bank_statement(
        bank_statement_input: BankStatementRequest,
        provider=Depends(get_provider)
) -> BankStatementShortResponse:

    handler = await provider.get_handler(
        key=bank_statement_input.operation_type
    )
    response = await handler.execute(bank_statement_input)
    return response
