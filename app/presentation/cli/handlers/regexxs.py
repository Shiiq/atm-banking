from enum import StrEnum
import re

from app.application.dto import BankStatementInput, DepositInput, WithdrawInput, BankOperationsFromInput

operations_pattern = r"bank[\s_]+statement|deposit|withdraw"
bank_statement_args_pattern = (
    r"(?P<operation_type>bank[\s_]?statement|deposit|withdraw)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<since>\d{4}[.-]\d{2}[.-]\d{2})\s+"
    r"(?P<till>\d{4}[.-]\d{2}[.-]\d{2})"
)
deposit_or_withdraw_args_pattern = (
    r"(?P<operation_type>bank[\s_]+statement|deposit|withdraw)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<amount>\d{1,7})"
)
operation_provider = {
    "deposit": {"pattern": deposit_or_withdraw_args_pattern,
                "parsed_data_model": BankOperationsFromInput.DEPOSIT},
    "withdraw": {"pattern": deposit_or_withdraw_args_pattern,
                 "parsed_data_model": BankOperationsFromInput.WITHDRAW},
    "bank statement": {"pattern": bank_statement_args_pattern,
                       "parsed_data_model": BankOperationsFromInput.BANK_STATEMENT},
    "bank_statement": {"pattern": bank_statement_args_pattern,
                       "parsed_data_model": BankOperationsFromInput.BANK_STATEMENT},
    "bankstatement": {"pattern": bank_statement_args_pattern,
                      "parsed_data_model": BankOperationsFromInput.BANK_STATEMENT},
}

operations = [
    input_bank_statement1 := " bank statement   ",
    # input_bank_statement2 := "  banKSTateMent ",
    input_bank_statement3 := "bank_statement   ",
    # input_bank_statement4 := " bank\nstatement",
    input_deposit := "   dEpoSit   ",
    input_withdraw := "   withdrAw ",
]
deposit_withdraw_and_args = [
    deposit_and_args := "   dEpoSit   lolo  vosk  2050 z",
    withdraw_and_args := " withdrAw  posa  keow  104010",
]
bank_statement_and_args = [
    bank_statement_and_args1 := " bank statement  lolo   vosk  2016-07-12 2019.03-21",
    bank_statement_and_args2 := "  banKSTateMent  lolo dvosk  2020-04-12    2005.05.01",
    bank_statement_and_args3 := "bank_statement lolo   vosk  2014.12.01   2015-12-06",
]

def check_operation_type(pattern, raw_data):
    decomposed_input = re.search(pattern, raw_data, flags=re.I)
    operation_type = decomposed_input.group().lower()


def parsing_deposit_withdraw_input(pattern, raw_data, output_model):
    decomposed_input = re.search(pattern, raw_data, flags=re.I)
    operation_type = decomposed_input.group("operation_type")
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


for i in bank_statement_and_args:
    print(parsing_bank_statement_input(bank_statement_args_pattern, i))
