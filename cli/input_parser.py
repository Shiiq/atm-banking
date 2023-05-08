from common.constants import BankOperationsFromInput

from common.database.models.dto_models import (BankStatementDTO,
                                               DepositDTO,
                                               WithdrawDTO)


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

    def parse_args(self, input_data: str) -> BankStatementDTO | DepositDTO | WithdrawDTO:
        operation, *args = input_data.strip().split()
        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            bank_statement_dto = self._get_bank_statement_operation_dto(operation.lower(),
                                                                        args)
            return bank_statement_dto

        elif operation.lower() in [BankOperationsFromInput.DEPOSIT,
                                   BankOperationsFromInput.WITHDRAW]:
            deposit_withdraw_dto = self._get_deposit_withdraw_operation_dto(operation.lower(),
                                                                            args)
            return deposit_withdraw_dto


    def _get_bank_statement_operation_dto(self, operation: str, args: list) -> BankStatementDTO:
        first_name, last_name, since, till = args
        return BankStatementDTO(operation=operation,
                                first_name=first_name.lower(),
                                last_name=last_name.lower(),
                                since=since,
                                till=till)

    def _get_deposit_withdraw_operation_dto(self, operation: str, args: list) -> DepositDTO | WithdrawDTO:
        first_name, last_name, amount = args
        if operation == BankOperationsFromInput.DEPOSIT:
            return DepositDTO(operation=operation,
                              first_name=first_name.lower(),
                              last_name=last_name.lower(),
                              amount=amount)
        elif operation == BankOperationsFromInput.WITHDRAW:
            return WithdrawDTO(operation=operation,
                               first_name=first_name.lower(),
                               last_name=last_name.lower(),
                               amount=amount)
