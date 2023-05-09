from cli.constants import BankOperationsFromInput
from common.database.models.dto_models import (BankStatementDTO,
                                               DepositDTO,
                                               WithdrawDTO)


class InputParserService:

    # input data examples
    # "withdraw jakes james 100500"
    # "deposit akoz pors 7000"

    def __init__(self):
        self._output_data = None

    def get_output_data(self, input_data: str) -> BankStatementDTO | DepositDTO | WithdrawDTO:
        self._parse_args(input_data)
        return self._output_data

    def _set_output_data(self, output_data: BankStatementDTO | DepositDTO | WithdrawDTO) -> None:
        self._output_data = output_data

    def _parse_args(self, input_data: str):
        operation, *args = input_data.strip().split()
        output_dto = None
        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            output_dto = self._get_bank_statement_operation_dto(operation.lower(),
                                                                args)
            # return bank_statement_dto

        elif operation.lower() == BankOperationsFromInput.DEPOSIT:
            output_dto = self._get_deposit_operation_dto(operation.lower(),
                                                         args)
            # return deposit_dto

        elif operation.lower() == BankOperationsFromInput.WITHDRAW:
            output_dto = self._get_withdraw_operation_dto(operation.lower(),
                                                          args)
            # return withdraw_dto
        else:
            raise Exception("Wrong operation")
        self._set_output_data(output_dto)

    def _get_bank_statement_operation_dto(self, operation: str, args: list) -> BankStatementDTO:
        first_name, last_name, since, till = args
        return BankStatementDTO(operation=operation,
                                first_name=first_name.lower(),
                                last_name=last_name.lower(),
                                since=since,
                                till=till)

    def _get_deposit_operation_dto(self, operation: str, args: list) -> DepositDTO:
        first_name, last_name, amount = args
        return DepositDTO(operation=operation,
                          first_name=first_name.lower(),
                          last_name=last_name.lower(),
                          amount=amount)

    def _get_withdraw_operation_dto(self, operation: str, args: list) -> WithdrawDTO:
        first_name, last_name, amount = args
        return WithdrawDTO(operation=operation,
                           first_name=first_name.lower(),
                           last_name=last_name.lower(),
                           amount=amount)
