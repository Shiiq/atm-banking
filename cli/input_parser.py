from common.constants import BankOperationsFromInput

from common.database.models.dto_models import BankStatementDTO, DepositOrWithdrawDTO


def parse_args(input_args: str) -> BankStatementDTO | DepositOrWithdrawDTO:
    operation, *args = input_args.strip().split()
    if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
        bank_statement_dto = _validate_bank_statement_operation(operation,
                                                                args)
        return bank_statement_dto
    elif operation.lower() in [BankOperationsFromInput.DEPOSIT,
                               BankOperationsFromInput.WITHDRAW]:
        deposit_withdraw_dto = _validate_deposit_withdraw_operation(operation,
                                                                    args)
        return deposit_withdraw_dto


def _validate_bank_statement_operation(operation: str, args: list) -> BankStatementDTO:
    first_name, last_name, since, till = args
    current_operation = BankStatementDTO(operation=operation.lower(),
                                         first_name=first_name.lower(),
                                         last_name=last_name.lower(),
                                         since=since,
                                         till=till)
    return current_operation


def _validate_deposit_withdraw_operation(operation: str, args: list) -> DepositOrWithdrawDTO:
    first_name, last_name, amount = args
    current_operation = DepositOrWithdrawDTO(operation=operation.lower(),
                                             first_name=first_name.lower(),
                                             last_name=last_name.lower(),
                                             amount=amount)
    return current_operation
