from fastapi import APIRouter, Depends
from starlette import status

from app.application.dto import DepositInput, FullOperationInfo
from app.presentation.api.dependencies import get_provider

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(
    path="/",
    responses={
        status.HTTP_200_OK: {
            "model": FullOperationInfo
        }
    },
    status_code=status.HTTP_200_OK
)
async def deposit(
        deposit_input: DepositInput,
        provider=Depends(get_provider)
) -> FullOperationInfo:

    handler = await provider.get_handler(
        key_class=deposit_input.operation_type
    )
    response = await handler.execute(deposit_input)
    return response
