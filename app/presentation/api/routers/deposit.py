from fastapi import APIRouter, Depends

from app.application.dto import DepositInput, SummaryOperationInfo
from app.application.operation_handlers import Deposit
from app.presentation.api.providers import Stub

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(path="/")
async def deposit(
        deposit_input: DepositInput,
        handler=Depends(Stub(Deposit))
) -> SummaryOperationInfo:
    response = await handler.execute(deposit_input)
    return response
