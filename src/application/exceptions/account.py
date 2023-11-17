from uuid import UUID

from .base import ApplicationException


class AccountIDNotExist(ApplicationException):

    def __init__(self, account_id: UUID):
        self.account_id = account_id

    @property
    def msg(self):
        return (
            f"An account with ID '{self.account_id}' does not exist"
        )

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg


class AccountHasInsufficientFunds(ApplicationException):

    def __init__(self, account_id: UUID):
        self.account_id = account_id

    @property
    def msg(self):
        return (
            f"An account with ID '{self.account_id}' has insufficient funds"
        )

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg
