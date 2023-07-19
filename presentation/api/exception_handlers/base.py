from fastapi import FastAPI

from application.exceptions import (AccountIDNotExist,
                                    AccountHasInsufficientFunds,
                                    CustomerIDNotExist,
                                    CustomerNotExist)
from .handlers import (account_id_not_exist_callback,
                       account_has_insufficient_funds_callback,
                       customer_id_not_exist_callback,
                       customer_not_exist_callback)


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(AccountIDNotExist, account_id_not_exist_callback)
    app.add_exception_handler(AccountHasInsufficientFunds, account_has_insufficient_funds_callback)
    app.add_exception_handler(CustomerIDNotExist, customer_id_not_exist_callback)
    app.add_exception_handler(CustomerNotExist, customer_not_exist_callback)
