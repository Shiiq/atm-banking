import re

from app.application.dto import (BankStatementInput,
                                 DepositInput,
                                 WithdrawInput,
                                 BankOperationsFromInput)
from app.presentation.cli.handlers.re_patterns import (OPERATION_PATTERN,
                                                       BANK_STATEMENT_PATTERN,
                                                       DEPOSIT_PATTERN,
                                                       WITHDRAW_PATTERN)


operation_provider = {
    # "operation type from cli": {"pattern for args",
    #                             "parsed data model"},
    "bank statement": {"args_pattern": BANK_STATEMENT_PATTERN,
                       "parsed_data_model": BankStatementInput},
    "bank_statement": {"args_pattern": BANK_STATEMENT_PATTERN,
                       "parsed_data_model": BankStatementInput},
    "bankstatement": {"args_pattern": BANK_STATEMENT_PATTERN,
                      "parsed_data_model": BankStatementInput},
    "deposit": {"args_pattern": DEPOSIT_PATTERN,
                "parsed_data_model": DepositInput},
    "withdraw": {"args_pattern": WITHDRAW_PATTERN,
                 "parsed_data_model": WithdrawInput},
}

operations_input = [
    input_bank_statement1 := " bank statement   ",
    # input_bank_statement2 := "  banKSTateMent ",
    input_bank_statement3 := "bank_statement   ",
    # input_bank_statement4 := " bank\nstatement",
    input_deposit := "   dEpoSit   ",
    input_withdraw := "   withdrAw ",
]
deposit_withdraw_and_args_input = [
    deposit_and_args := "   dEposit   lolo  vosk  2050 z",
    withdraw_and_args := " withdraw  posa  keow  104010",
]
bank_statement_and_args_input = [
    bank_statement_and_args1 := " bank statement  lolo   vosk  2016-07-12 2019.03-21",
    bank_statement_and_args2 := "  bankstatement  lolo dvosk  2020-04-12    2005.05.01",
    bank_statement_and_args3 := "bank_statement lolo   vosk  2014.12.01   2015-12-06",
]
all_in_one_input = [*bank_statement_and_args_input, *deposit_withdraw_and_args_input]


def parsing_deposit_withdraw_input(pattern, raw_data, output_model):
    decomposed_input = re.search(pattern, raw_data, flags=re.I)
    first_name = decomposed_input.group("first_name")
    last_name = decomposed_input.group("last_name")
    amount = decomposed_input.group("amount")
    return output_model(first_name=first_name,
                        last_name=last_name,
                        amount=amount)


def parsing_bank_statement_input(pattern, raw_data, output_model):
    decomposed_input = re.search(pattern, raw_data, flags=re.I)
    first_name = decomposed_input.group("first_name")
    last_name = decomposed_input.group("last_name")
    since = decomposed_input.group("since")
    till = decomposed_input.group("till")

    since = re.sub(r"(\d{4})[.-](\d{2})[.-](\d{2})", r"\1-\2-\3", since)
    till = re.sub(r"(\d{4})[.-](\d{2})[.-](\d{2})", r"\1-\2-\3", till)
    return output_model(first_name=first_name,
                        last_name=last_name,
                        since=since,
                        till=till)


def check_operation_type(pattern, raw_data):
    decomposed_input = re.search(pattern, raw_data, flags=re.I)
    if not decomposed_input:
        raise Exception("WRONG OPERATION")
    operation_type = decomposed_input.group().lower()
    operation_type = re.sub(r"bank[\s_]?statement", r"bank_statement", operation_type)
    # print(operation_type, type(operation_type))
    pattern = operation_provider.get(operation_type).get("args_pattern")
    output_model = operation_provider.get(operation_type).get("parsed_data_model")
    if operation_type == BankOperationsFromInput.BANK_STATEMENT:
        return parsing_bank_statement_input(pattern=pattern,
                                            raw_data=raw_data,
                                            output_model=output_model)
    elif operation_type == BankOperationsFromInput.DEPOSIT or BankOperationsFromInput.WITHDRAW:
        return parsing_deposit_withdraw_input(pattern=pattern,
                                              raw_data=raw_data,
                                              output_model=output_model)

from pprint import pprint

for i in all_in_one_input:
    pprint(check_operation_type(OPERATION_PATTERN, i).model_dump_json())
