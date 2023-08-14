import re
from re import Pattern
from typing import Type

from app.application.dto import (BankOperationsInput,
                                 BankStatementInput,
                                 DepositInput,
                                 WithdrawInput)
from app.presentation.cli.common import (ExitCommand,
                                         ExitOperation,
                                         InputDataError,
                                         WrongOperationError)
from app.presentation.cli.handlers.re_patterns import (OPERATION_TYPES_PATTERN,
                                                       BANK_STATEMENT_OPERATION_PATTERN,
                                                       DEPOSIT_OPERATION_PATTERN,
                                                       WITHDRAW_OPERATION_PATTERN,
                                                       BANK_STATEMENT_VARIATIONS_PATTERN,
                                                       REPL_BANK_STATEMENT_PATTERN,
                                                       DATE_VARIATIONS_PATTERN,
                                                       REPL_DATE_PATTERN)


class InputHandler:

    _OPERATION_TYPE_MAPPING = {
        "bank statement": BankOperationsInput.BANK_STATEMENT,
        "bank_statement": BankOperationsInput.BANK_STATEMENT,
        "bankstatement": BankOperationsInput.BANK_STATEMENT,
        "deposit": BankOperationsInput.DEPOSIT,
        "withdraw": BankOperationsInput.WITHDRAW
    }

    _OPERATION_PARAM_MAPPING = {
        BankOperationsInput.BANK_STATEMENT: {
            "args_pattern": BANK_STATEMENT_OPERATION_PATTERN,
            "parsed_data_model": BankStatementInput
        },
        BankOperationsInput.DEPOSIT: {
            "args_pattern": DEPOSIT_OPERATION_PATTERN,
            "parsed_data_model": DepositInput
        },
        BankOperationsInput.WITHDRAW: {
            "args_pattern": WITHDRAW_OPERATION_PATTERN,
            "parsed_data_model": WithdrawInput
        },
    }

    def _check_operation_type(
            self,
            raw_data: str
    ) -> BankOperationsInput:

        parsed_input = re.search(pattern=OPERATION_TYPES_PATTERN,
                                 string=raw_data)
        if not parsed_input:
            # logging wrong operation
            raise WrongOperationError("Wrong operation")

        operation_type = parsed_input.group()
        if operation_type == ExitCommand.EXIT:
            # logging exit operation
            raise ExitOperation("Exiting")

        operation_type = re.sub(pattern=BANK_STATEMENT_VARIATIONS_PATTERN,
                                repl=REPL_BANK_STATEMENT_PATTERN,
                                string=operation_type)
        return self._OPERATION_TYPE_MAPPING[operation_type]

    def _parse(
            self,
            raw_data: str
    ) -> BankStatementInput | DepositInput | WithdrawInput:

        operation_type = self._check_operation_type(raw_data)
        args_pattern = (self._OPERATION_PARAM_MAPPING
                        .get(operation_type)
                        .get("args_pattern"))
        parsed_data_model = (self._OPERATION_PARAM_MAPPING
                             .get(operation_type)
                             .get("parsed_data_model"))
        if operation_type == BankOperationsInput.BANK_STATEMENT:
            return self._bank_statement(pattern=args_pattern,
                                        raw_data=raw_data,
                                        data_model=parsed_data_model)
        elif operation_type == BankOperationsInput.DEPOSIT or BankOperationsInput.WITHDRAW:
            return self._deposit_or_withdraw(pattern=args_pattern,
                                             raw_data=raw_data,
                                             data_model=parsed_data_model)

    def _bank_statement(
            self,
            pattern: Pattern[str],
            raw_data: str,
            data_model: Type[BankStatementInput]
    ) -> BankStatementInput:

        parsed_data = re.search(pattern=pattern,
                                string=raw_data)
        if not parsed_data:
            raise InputDataError("Incorrect data has been entered")
        first_name = parsed_data.group("first_name")
        last_name = parsed_data.group("last_name")
        since = re.sub(pattern=DATE_VARIATIONS_PATTERN,
                       repl=REPL_DATE_PATTERN,
                       string=parsed_data.group("since"))
        till = re.sub(pattern=DATE_VARIATIONS_PATTERN,
                      repl=REPL_DATE_PATTERN,
                      string=parsed_data.group("till"))

        return data_model(first_name=first_name,
                          last_name=last_name,
                          since=since,
                          till=till)

    def _deposit_or_withdraw(
            self,
            pattern: Pattern[str],
            raw_data: str,
            data_model: Type[DepositInput | WithdrawInput]
    ) -> DepositInput | WithdrawInput:

        parsed_data = re.search(pattern=pattern,
                                string=raw_data)
        if not parsed_data:
            raise InputDataError("Incorrect data has been entered")
        first_name = parsed_data.group("first_name")
        last_name = parsed_data.group("last_name")
        amount = parsed_data.group("amount")

        return data_model(first_name=first_name,
                          last_name=last_name,
                          amount=amount)

    def parse(
            self,
            input_data: str
    ) -> BankStatementInput | DepositInput | WithdrawInput:

        return self._parse(raw_data=input_data.lower())


# ih = InputHandler()
# bank_statement_and_args_input = [
#     " bank statement  lolo   vosk  2016-07-12 2019.03-21",
#     "  bankstatement  lolo dvosk  2020-04-12    2005.05.01",
#     "bank_statement lolo   vosk  2014.12.01   2015-12-06",
# ]
# deposit_withdraw_and_args_input = [
#     "   dEposit   lolo  vosk  2050 z",
#     " withdraw  posa  keow  104010",
# ]
#
# all_in_one_input = [*bank_statement_and_args_input, *deposit_withdraw_and_args_input]
#
# for i in all_in_one_input:
#     print(ih.parse_input(i))
