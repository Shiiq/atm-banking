

class AccountHasInsufficientFunds(Exception):

    def __init__(self, account_id: int):
        self.account_id = account_id

    @property
    def message(self):
        return f"An account with ID '{self.account_id}' has insufficient funds to withdraw"

    def __str__(self):
        return self.message
