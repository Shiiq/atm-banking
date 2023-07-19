from typing import Generic, TypeVar

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, ORJSONResponse
from pydantic import BaseModel, ConfigDict
from starlette import status

from application.exceptions import (AccountIDNotExist,
                                    AccountHasInsufficientFunds,
                                    CustomerIDNotExist,
                                    CustomerNotExist)

Exc = TypeVar("Exc")


class ExceptionData(BaseModel, Generic[Exc]):

    model_config = ConfigDict(arbitrary_types_allowed=True)
    exc_message: str
    exc_body: Exc


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


async def convert_exception_to_json(request, status_code, error):
    print(error)
    return JSONResponse(
        content=ExceptionData(exc_message=error.message, exc_body=error),
        status_code=status_code
    )
