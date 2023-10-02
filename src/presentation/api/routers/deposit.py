from fastapi import APIRouter, Depends
from starlette import status

from src.application.dto import DepositInput, ShortOperationInfo
from src.presentation.api.dependencies import get_provider

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(
    path="/",
    response_model=ShortOperationInfo,
    status_code=status.HTTP_200_OK
)
async def deposit(
        deposit_input: DepositInput,
        provider=Depends(get_provider)
) -> ShortOperationInfo:

    handler = await provider.get_handler(
        key_class=deposit_input.operation_type
    )
    response = await handler.execute(deposit_input)
    return response
