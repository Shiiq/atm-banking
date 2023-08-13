import re

from app.application.dto import (BankOperationsFromInput,
                                 BankStatementInput,
                                 DepositInput,
                                 WithdrawInput)
from app.presentation.cli.common import ExitCommand, ExitOperation, WrongOperationError
from app.presentation.cli.handlers.re_patterns import (OPERATION_PATTERN,
                                                       BANK_STATEMENT_PATTERN,
                                                       DEPOSIT_PATTERN,
                                                       WITHDRAW_PATTERN,
                                                       BANK_STATEMENT_VARIATIONS_PATTERN,
                                                       REPL_BANK_STATEMENT_PATTERN,
                                                       DATE_VARIATIONS_PATTERN,
                                                       REPL_DATE_PATTERN)


class InputHandler:

    _DTO_MAPPING = {
        "bank statement": BankOperationsFromInput.BANK_STATEMENT,
        "bank_statement": BankOperationsFromInput.BANK_STATEMENT,
        "bankstatement": BankOperationsFromInput.BANK_STATEMENT,
        "deposit": BankOperationsFromInput.DEPOSIT,
        "withdraw": BankOperationsFromInput.WITHDRAW
    }

    _OPERATIONS_MAPPING = {
        BankOperationsFromInput.BANK_STATEMENT: {
            "args_pattern": BANK_STATEMENT_PATTERN,
            "parsed_data_model": BankStatementInput
        },
        BankOperationsFromInput.DEPOSIT: {
            "args_pattern": DEPOSIT_PATTERN,
            "parsed_data_model": DepositInput
        },
        BankOperationsFromInput.WITHDRAW: {
            "args_pattern": WITHDRAW_PATTERN,
            "parsed_data_model": WithdrawInput
        },
    }

    def _check_operation_type(self, raw_data: str):
        parsed_input = re.search(pattern=OPERATION_PATTERN,
                                 string=raw_data,
                                 flags=re.I)
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
        return self._DTO_MAPPING[operation_type]

    def _parse_input(self, raw_data: str):
        # TODO CHECK ALL DATA IS VALID
        operation_type = self._check_operation_type(raw_data)
        args_pattern = self._OPERATIONS_MAPPING.get(operation_type).get("args_pattern")
        parsed_data_model = self._OPERATIONS_MAPPING.get(operation_type).get("parsed_data_model")
        if operation_type == BankOperationsFromInput.BANK_STATEMENT:
            return self._bank_statement(pattern=args_pattern,
                                        raw_data=raw_data,
                                        data_model=parsed_data_model)
        elif operation_type == BankOperationsFromInput.DEPOSIT or BankOperationsFromInput.WITHDRAW:
            return self._deposit_or_withdraw(pattern=args_pattern,
                                             raw_data=raw_data,
                                             data_model=parsed_data_model)

    def _bank_statement(self, pattern, raw_data, data_model):
        # TODO CHECK ALL DATA IS VALID
        parsed_data = re.search(pattern, raw_data, flags=re.I)
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

    def _deposit_or_withdraw(self, pattern, raw_data, data_model):
        # TODO CHECK ALL DATA IS VALID
        parsed_data = re.search(pattern=pattern, string=raw_data, flags=re.I)
        first_name = parsed_data.group("first_name")
        last_name = parsed_data.group("last_name")
        amount = parsed_data.group("amount")

        return data_model(first_name=first_name,
                          last_name=last_name,
                          amount=amount)

    def parse_input(self, input_data):
        return self._parse_input(raw_data=input_data.lower())


ih = InputHandler()
bank_statement_and_args_input = [
    bank_statement_and_args1 := " bank statement  lolo   vosk  2016-07-12 2019.03-21",
    bank_statement_and_args2 := "  bankstatement  lolo dvosk  2020-04-12    2005.05.01",
    bank_statement_and_args3 := "bank_statement lolo   vosk  2014.12.01   2015-12-06",
]
deposit_withdraw_and_args_input = [
    deposit_and_args := "   dEposit   lolo  vosk  2050 z",
    withdraw_and_args := " withdraw  posa  keow  104010",
]
all_in_one_input = [*bank_statement_and_args_input, *deposit_withdraw_and_args_input]

for i in all_in_one_input:
    print(ih.parse_input(i))
