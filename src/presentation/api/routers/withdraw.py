from fastapi import APIRouter, Depends
from starlette import status

from src.application.dto import WithdrawInput, ShortOperationInfo
from src.presentation.api.dependencies import get_provider

withdraw_router = APIRouter(prefix="/withdraw")


@withdraw_router.post(
    path="/",
    response_model=ShortOperationInfo,
    status_code=status.HTTP_200_OK
)
async def withdraw(
        withdraw_input: WithdrawInput,
        provider=Depends(get_provider)
) -> ShortOperationInfo:

    handler = await provider.get_handler(
        key=withdraw_input.operation_type
    )
    response = await handler.execute(withdraw_input)
    return response
