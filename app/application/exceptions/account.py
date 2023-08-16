from .base import ApplicationException


class AccountIDNotExist(ApplicationException):

    def __init__(self, account_id: int):
        self.account_id = account_id

    @property
    def msg(self):
        return f"An account with ID '{self.account_id}' does not exist"

    def __str__(self):
        return self.msg


class AccountHasInsufficientFunds(ApplicationException):

    def __init__(self, account_id: int):
        self.account_id = account_id

    @property
    def msg(self):
        return f"An account with ID '{self.account_id}' has insufficient funds to withdraw"

    def __str__(self):
        return self.msg
