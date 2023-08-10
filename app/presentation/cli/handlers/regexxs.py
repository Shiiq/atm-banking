from enum import StrEnum
import re

from app.application.dto import BankStatementInput, DepositInput, WithdrawInput


# class BankOperationsInput(StrEnum):
#
#     DEPOSIT = "deposit"
#     WITHDRAW = "withdraw"
#     BANK_STATEMENT = "bank_statement"
#
#
# operation_provider = {
#     "deposit": BankOperationsInput.DEPOSIT,
#     "withdraw": BankOperationsInput.WITHDRAW,
#     "bank_statement": BankOperationsInput.BANK_STATEMENT,
#     "bankstatement": BankOperationsInput.BANK_STATEMENT,
#     "bank statement": BankOperationsInput.BANK_STATEMENT
# }

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
    bank_statement_and_args1 := " bank statement  lolo   vosk  2050-02-12 2019.31-21",
    bank_statement_and_args2 := "  banKSTateMent  lolo dvosk  2050-12-12    1233.05.01",
    bank_statement_and_args3 := "bank_statement lolo   vosk  2014.12.01   2015-12-06",
    # input_bank_statement4 := " bank\nstatement",
]


def parsing_deposit_withdraw_input(pattern, input_str):
    ...


def parsing_bank_statement_input(pattern, input_str):
    decomposite = re.search(pattern, input_str, flags=re.I)
    operation_type = decomposite.group("operation_type").lower()
    first_name = decomposite.group("first_name")
    last_name = decomposite.group("last_name")
    since = decomposite.group("since")
    till = decomposite.group("till")
    p = r"(\d{4})[.-](\d{2})[.-](\d{2})"
    print(re.sub(p, r"\1-\2-\3", since))
    # since = re.sub(r"\d{4}[.-]\d{2}[.-]\d{2}", r"\d{4}-\d{2}-\d{2}", since)
    # till = re.sub("r\d{4}[.-]\d{2}[.-]\d{2}", r"\d{4}-\d{2}-\d{2}", till)
    # output = BankStatementInput(first_name=first_name,
    #                             last_name=last_name,
    #                             since=since,
    #                             till=till)
    # return output


for i in bank_statement_and_args:
    print(parsing_bank_statement_input(bank_statement_args_pattern, i))
