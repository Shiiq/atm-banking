from typing import Annotated

from fastapi import APIRouter, Depends

from application.usecases import Deposit, IUsecase
from infrastructure.database.models.dto import DepositInput, SummaryOperationInfo
from infrastructure.provider import Provider
from presentation.api.providers import Stub

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(path="/")
async def deposit(
        deposit_input: DepositInput,
        provider=Depends(Stub(Deposit))
) -> SummaryOperationInfo:
    res = await provider(deposit_input)
    return res
