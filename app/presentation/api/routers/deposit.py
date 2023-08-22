from fastapi import APIRouter, Depends

from app.application.dto import DepositInput, SummaryOperationInfo
from app.presentation.api.dependencies import get_provider

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(path="/")
async def deposit(
        deposit_input: DepositInput,
        provider=Depends(get_provider)
) -> SummaryOperationInfo:

    handler = await provider.get_handler(
        key_class=deposit_input.operation_type
    )
    response = await handler.execute(deposit_input)
    return response
