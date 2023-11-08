import re
from re import Pattern
from typing import Type

from src.application.dto import BankOperationType
from src.application.dto import BankStatementRequest
from src.application.dto import DepositRequest
from src.application.dto import WithdrawRequest
from src.presentation.cli.common.commands import ExitCommand
from src.presentation.cli.common.exceptions import ExitOperation
from src.presentation.cli.common.exceptions import InputDataError
from src.presentation.cli.common.exceptions import WrongOperationError
from .re_patterns import OPERATION_TYPES_PATTERN
from .re_patterns import BANK_STATEMENT_OPERATION_PATTERN
from .re_patterns import DEPOSIT_OPERATION_PATTERN
from .re_patterns import WITHDRAW_OPERATION_PATTERN
from .re_patterns import BANK_STATEMENT_VARIATIONS_PATTERN
from .re_patterns import REPL_BANK_STATEMENT_PATTERN
from .re_patterns import DATE_VARIATIONS_PATTERN
from .re_patterns import REPL_DATE_PATTERN


class InputHandler:

    _OPERATION_TYPES_MAPPING = {
        "bank_statement": BankOperationType.BANK_STATEMENT,
        "deposit": BankOperationType.DEPOSIT,
        "withdraw": BankOperationType.WITHDRAW
    }

    _OPERATION_PARAMS_MAPPING = {
        BankOperationType.BANK_STATEMENT: {
            "args_pattern": BANK_STATEMENT_OPERATION_PATTERN,
            "operation_data_model": BankStatementRequest
        },
        BankOperationType.DEPOSIT: {
            "args_pattern": DEPOSIT_OPERATION_PATTERN,
            "operation_data_model": DepositRequest
        },
        BankOperationType.WITHDRAW: {
            "args_pattern": WITHDRAW_OPERATION_PATTERN,
            "operation_data_model": WithdrawRequest
        },
    }

    def parse(
            self,
            input_data: str
    ) -> BankStatementRequest | DepositRequest | WithdrawRequest:
        return self._parse(raw_data=input_data.lower())

    def _parse(
            self,
            raw_data: str
    ) -> BankStatementRequest | DepositRequest | WithdrawRequest:

        operation_type = self._check_operation_type(raw_data)
        operation_params = self._OPERATION_PARAMS_MAPPING[operation_type]
        args_pattern = operation_params["args_pattern"]
        data_model = operation_params["operation_data_model"]

        if operation_type == BankOperationType.BANK_STATEMENT:
            return self._bank_statement(
                pattern=args_pattern,
                raw_data=raw_data,
                data_model=data_model
            )
        elif (operation_type == BankOperationType.DEPOSIT
              or operation_type == BankOperationType.WITHDRAW):
            return self._deposit_or_withdraw(
                pattern=args_pattern,
                raw_data=raw_data,
                data_model=data_model
            )

    def _check_operation_type(
            self,
            raw_data: str
    ) -> BankOperationType:

        parsed_input = re.search(
            pattern=OPERATION_TYPES_PATTERN,
            string=raw_data
        )
        if not parsed_input:
            raise WrongOperationError

        operation_type = parsed_input.group()
        if operation_type == ExitCommand.EXIT:
            raise ExitOperation

        # adds underscore between to the string value
        # if operation "bank statement" or "bankstatement"
        # e.g. "bank statement" or "bankstatement" will become "bank_statement"
        # or nothing will happen for the other types of operations
        operation_type = re.sub(
            pattern=BANK_STATEMENT_VARIATIONS_PATTERN,
            repl=REPL_BANK_STATEMENT_PATTERN,
            string=operation_type
        )
        return self._OPERATION_TYPES_MAPPING[operation_type]

    def _bank_statement(
            self,
            pattern: Pattern[str],
            raw_data: str,
            data_model: Type[BankStatementRequest]
    ) -> BankStatementRequest:

        parsed_data = re.search(pattern=pattern, string=raw_data)
        if not parsed_data:
            raise InputDataError

        # converts date format from "DD-MM-YYYY" to "YYYY-MM-DD"
        # e.g. "31-01-2023" will transform to "2023-01-31"
        since = re.sub(
            pattern=DATE_VARIATIONS_PATTERN,
            repl=REPL_DATE_PATTERN,
            string=parsed_data.group("since")
        )
        till = re.sub(
            pattern=DATE_VARIATIONS_PATTERN,
            repl=REPL_DATE_PATTERN,
            string=parsed_data.group("till")
        )
        first_name = parsed_data.group("first_name")
        last_name = parsed_data.group("last_name")
        return data_model(
            first_name=first_name,
            last_name=last_name,
            since=since,
            till=till
        )

    def _deposit_or_withdraw(
            self,
            pattern: Pattern[str],
            raw_data: str,
            data_model: Type[DepositRequest | WithdrawRequest]
    ) -> DepositRequest | WithdrawRequest:

        parsed_data = re.search(pattern=pattern, string=raw_data)
        if not parsed_data:
            raise InputDataError

        first_name = parsed_data.group("first_name")
        last_name = parsed_data.group("last_name")
        amount = parsed_data.group("amount")
        return data_model(
            first_name=first_name,
            last_name=last_name,
            amount=amount
        )
