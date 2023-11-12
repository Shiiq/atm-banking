from typing import Generic, TypeVar

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from starlette import status

from src.application.exceptions import AccountIDNotExist
from src.application.exceptions import AccountHasInsufficientFunds
from src.application.exceptions import CustomerIDNotExist
from src.application.exceptions import CustomerNotExist
from src.infrastructure.unit_of_work import UnitOfWorkError

ExcDataT = TypeVar("ExcDataT")


class ExceptionData(BaseModel, Generic[ExcDataT]):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True
    )

    error_message: str
    error_body: ExcDataT


async def account_id_not_exist_callback(
        request: Request,
        error: AccountIDNotExist
):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def account_has_insufficient_funds_callback(
        request: Request,
        error: AccountHasInsufficientFunds
):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def customer_id_not_exist_callback(
        request: Request,
        error: CustomerIDNotExist
):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def customer_not_exist_callback(
        request: Request,
        error: CustomerNotExist
):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def unit_of_work_error_callback(
        request: Request,
        error: UnitOfWorkError
):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def convert_exception_to_json(
        request: Request,
        status_code: int, error
):
    return JSONResponse(
        content=ExceptionData(
            error_message=error.msg,
            error_body=error
        )
        .model_dump(exclude={"error_body"}),
        status_code=status_code
    )
