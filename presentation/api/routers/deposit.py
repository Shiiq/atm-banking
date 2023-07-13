from typing import Annotated

from fastapi import APIRouter, Depends

from application.usecases import Deposit, IUsecase
from infrastructure.database.models.dto import DepositInput, SummaryOperationInfo
from infrastructure.mediator import Mediator
from presentation.api.providers import Stub

deposit_router = APIRouter(prefix="/deposit")


@deposit_router.post(path="/")
async def deposit(
        deposit_input: DepositInput,
        mediator: Annotated[IUsecase, Depends(Stub(Mediator))]
) -> SummaryOperationInfo:
    res = await mediator(deposit_input)
    return res
