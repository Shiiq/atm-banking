from application.usecases import BankStatement, Deposit, Withdraw
from infrastructure.database.models.constants import BankOperationsFromInput


class OperationMediator:

    def __init__(self):

        self._operations_mapping = {
            BankOperationsFromInput.BANK_STATEMENT: BankStatement,
            BankOperationsFromInput.DEPOSIT: Deposit,
            BankOperationsFromInput.WITHDRAW: Withdraw
        }

    def get_operation_handler(self, operation: BankOperationsFromInput):
        return self._operations_mapping.get(operation)
