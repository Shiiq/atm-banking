from application.usecases import BankStatement, Deposit, Withdraw


class DIContainer:

    def __init__(self, container, executor):

        self._container = container
        self._executor = executor
        self._operations_mapping = {
            "bank_statement": BankStatement,
            "deposit": Deposit,
            "withdraw": Withdraw
        }

    async def execute(self):
        ...
