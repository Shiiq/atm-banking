from fastapi import APIRouter, Depends
from starlette import status

from src.application.dto import DepositRequest, OperationShortResponse
from src.presentation.api.dependencies import get_provider

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(
    path="/",
    response_model=OperationShortResponse,
    status_code=status.HTTP_200_OK
)
async def deposit(
        deposit_input: DepositRequest,
        provider=Depends(get_provider)
) -> OperationShortResponse:

    handler = await provider.get_handler(
        key=deposit_input.operation_type
    )
    response = await handler.execute(deposit_input)
    return response
