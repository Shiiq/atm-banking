from fastapi import FastAPI

from src.application.exceptions import AccountIDNotExist
from src.application.exceptions import AccountHasInsufficientFunds
from src.application.exceptions import CustomerIDNotExist
from src.application.exceptions import CustomerNotExist
from src.infrastructure.unit_of_work import UnitOfWorkError
from .handlers import account_id_not_exist_callback
from .handlers import account_has_insufficient_funds_callback
from .handlers import customer_id_not_exist_callback
from .handlers import customer_not_exist_callback
from .handlers import unit_of_work_error_callback


def setup_exception_handlers(app: FastAPI):

    app.add_exception_handler(
        AccountIDNotExist,
        account_id_not_exist_callback
    )
    app.add_exception_handler(
        AccountHasInsufficientFunds,
        account_has_insufficient_funds_callback
    )
    app.add_exception_handler(
        CustomerIDNotExist,
        customer_id_not_exist_callback
    )
    app.add_exception_handler(
        CustomerNotExist,
        customer_not_exist_callback
    )
    app.add_exception_handler(
        UnitOfWorkError,
        unit_of_work_error_callback
    )
