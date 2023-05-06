from common.constants import BankOperationsFromInput

from common.database.models.dto_models import BankStatementDTO, DepositOrWithdrawDTO


class InputParserService:

    # data = "withdraw jakes james 100500"
    # data = "deposit akoz pors 7000"

    def __init__(self, input_data: str):
        self._input_data = input_data
        self.__output_data = None

    def get_output_data(self):
        return self.__output_data

    def __set_output_data(self, output_data):
        self.__output_data = output_data

    def parse_args(self, input_data: str) -> BankStatementDTO | DepositOrWithdrawDTO:
        operation, *args = input_data.strip().split()
        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            bank_statement_dto = self._validate_bank_statement_operation(operation,
                                                                    args)
            return bank_statement_dto
        elif operation.lower() in [BankOperationsFromInput.DEPOSIT,
                                   BankOperationsFromInput.WITHDRAW]:
            deposit_withdraw_dto = self._validate_deposit_withdraw_operation(operation,
                                                                             args)
            return deposit_withdraw_dto


    def _validate_bank_statement_operation(self, operation: str, args: list) -> BankStatementDTO:
        first_name, last_name, since, till = args
        current_operation = BankStatementDTO(operation=operation.lower(),
                                             first_name=first_name.lower(),
                                             last_name=last_name.lower(),
                                             since=since,
                                             till=till)
        return current_operation


    def _validate_deposit_withdraw_operation(self, operation: str, args: list) -> DepositOrWithdrawDTO:
        first_name, last_name, amount = args
        current_operation = DepositOrWithdrawDTO(operation=operation.lower(),
                                                 first_name=first_name.lower(),
                                                 last_name=last_name.lower(),
                                                 amount=amount)
        return current_operation
