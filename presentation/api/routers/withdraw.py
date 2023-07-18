from fastapi import APIRouter, Depends

from application.usecases import Withdraw
from application.dto import WithdrawInput, SummaryOperationInfo
from presentation.api.providers import Stub

withdraw_router = APIRouter(prefix="/withdraw")


@withdraw_router.post(path="/")
async def withdraw(
        withdraw_input: WithdrawInput,
        handler=Depends(Stub(Withdraw))
) -> SummaryOperationInfo:
    response = await handler(withdraw_input)
    return response
