from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette import status

from application.exceptions import (AccountIDNotExist,
                                    AccountHasInsufficientFunds,
                                    CustomerIDNotExist,
                                    CustomerNotExist)


class ExceptionData(BaseModel):

    exc_message: str
    exc_body: Exception


def setup_exception_handlers(app: FastAPI):

    pass


async def account_id_not_exist_callback(request: Request, error: AccountIDNotExist):
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
    return JSONResponse(
        ExceptionData(exc_message=error.message, data=error),
        status_code=status_code
    )
