from fastapi import FastAPI

from app.application.exceptions import (AccountIDNotExist,
                                        AccountHasInsufficientFunds,
                                        CustomerIDNotExist,
                                        CustomerNotExist)
from app.infrastructure.unit_of_work import UnitOfWorkError
from .handlers import (account_id_not_exist_callback,
                       account_has_insufficient_funds_callback,
                       customer_id_not_exist_callback,
                       customer_not_exist_callback,
                       unit_of_work_error_callback)


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(AccountIDNotExist, account_id_not_exist_callback)
    app.add_exception_handler(AccountHasInsufficientFunds, account_has_insufficient_funds_callback)
    app.add_exception_handler(CustomerIDNotExist, customer_id_not_exist_callback)
    app.add_exception_handler(CustomerNotExist, customer_not_exist_callback)
    app.add_exception_handler(UnitOfWorkError, unit_of_work_error_callback)
