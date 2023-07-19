from fastapi import APIRouter, Depends

from application.dto import DepositInput, SummaryOperationInfo
from application.operation_handlers import Deposit
from presentation.api.providers import Stub

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(path="/")
async def deposit(
        deposit_input: DepositInput,
        handler=Depends(Stub(Deposit))
) -> SummaryOperationInfo:
    response = await handler(deposit_input)
    return response
