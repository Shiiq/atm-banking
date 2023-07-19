from typing import Generic, TypeVar

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from starlette import status

from application.exceptions import (AccountIDNotExist,
                                    AccountHasInsufficientFunds,
                                    CustomerIDNotExist,
                                    CustomerNotExist)
from infrastructure.unit_of_work import UnitOfWorkError

Exc = TypeVar("Exc")


class ExceptionData(BaseModel, Generic[Exc]):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True
    )

    error_message: str
    error_data: Exc


async def account_id_not_exist_callback(request: Request, error: AccountIDNotExist):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def account_has_insufficient_funds_callback(request: Request, error: AccountHasInsufficientFunds):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )

async def customer_id_not_exist_callback(request: Request, error: CustomerIDNotExist):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def customer_not_exist_callback(request: Request, error: CustomerNotExist):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )


async def unit_of_work_error_callback(request: Request, error: UnitOfWorkError):
    return await convert_exception_to_json(
        request=request,
        status_code=status.HTTP_404_NOT_FOUND,
        error=error
    )

async def convert_exception_to_json(request: Request, status_code: int, error):
    return JSONResponse(
        content=ExceptionData(error_message=error.message,
                              error_data=error)
        .model_dump(exclude={"error_data"}),
        status_code=status_code
    )
