from typing import Union

from fastapi import APIRouter, Depends
from starlette import status

from app.application.dto import WithdrawInput, SummaryOperationInfo
from app.application.exceptions import (AccountIDNotExist,
                                        AccountHasInsufficientFunds,
                                        CustomerIDNotExist,
                                        CustomerNotExist)
from app.application.operation_handlers import Withdraw
from app.presentation.api.exception_handlers import ExceptionData
from app.presentation.api.providers import Stub

withdraw_router = APIRouter(prefix="/withdraw")


@withdraw_router.post(
    path="/",
    responses={
        status.HTTP_200_OK: {
            "model": SummaryOperationInfo
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ExceptionData[
                Union[AccountIDNotExist, AccountHasInsufficientFunds, CustomerIDNotExist, CustomerNotExist]
            ]
        }
    },
    status_code=status.HTTP_200_OK
)
async def withdraw(
        withdraw_input: WithdrawInput,
        handler=Depends(Stub(Withdraw))
) -> SummaryOperationInfo:
    response = await handler.execute(withdraw_input)
    return response
