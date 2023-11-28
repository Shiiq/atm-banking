from fastapi import APIRouter, Depends
from starlette import status

from atm_banking.application.dto import WithdrawRequest
from atm_banking.application.dto import OperationShortResponse
from atm_banking.presentation.api.dependencies import get_provider

withdraw_router = APIRouter(prefix="/withdraw")


@withdraw_router.post(
    path="/",
    response_model=OperationShortResponse,
    status_code=status.HTTP_200_OK
)
async def withdraw(
        withdraw_input: WithdrawRequest,
        provider=Depends(get_provider)
) -> OperationShortResponse:

    handler = await provider.get_handler(
        key=withdraw_input.operation_type
    )
    response = await handler.execute(withdraw_input)
    return response
