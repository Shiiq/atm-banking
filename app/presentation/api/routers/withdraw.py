from typing import Union

from fastapi import APIRouter, Depends
from starlette import status

from app.application.dto import WithdrawInput, FullOperationInfo
from app.application.exceptions import (AccountIDNotExist,
                                        AccountHasInsufficientFunds,
                                        CustomerIDNotExist,
                                        CustomerNotExist)
from app.presentation.api.exception_handlers import ExceptionData
from app.presentation.api.dependencies import get_provider

withdraw_router = APIRouter(prefix="/withdraw")


@withdraw_router.post(
    path="/",
    responses={
        status.HTTP_200_OK: {
            "model": FullOperationInfo
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ExceptionData[
                Union[AccountIDNotExist,
                      AccountHasInsufficientFunds,
                      CustomerIDNotExist,
                      CustomerNotExist]
            ]
        }
    },
    status_code=status.HTTP_200_OK
)
async def withdraw(
        withdraw_input: WithdrawInput,
        provider=Depends(get_provider)
) -> FullOperationInfo:

    handler = await provider.get_handler(
        key_class=withdraw_input.operation_type
    )
    response = await handler.execute(withdraw_input)
    return response
