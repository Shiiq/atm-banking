from uuid import UUID

from .base import ApplicationException


class AccountIDNotExist(ApplicationException):

    def __init__(self, account_id: UUID):
        self.account_id = account_id

    @property
    def msg(self):
        return f"An account with ID '{self.account_id}' does not exist"

    @property
    def ui_msg(self):
        return self.msg


class AccountHasInsufficientFunds(ApplicationException):

    def __init__(self, account_id: UUID):
        self.account_id = account_id

    @property
    def msg(self):
        return f"An account with ID '{self.account_id}' has insufficient funds"

    @property
    def ui_msg(self):
        return self.msg