from enum import StrEnum
import re


class BankOperationsInput(StrEnum):

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


operation_provider = {
    "deposit": BankOperationsInput.DEPOSIT,
    "withdraw": BankOperationsInput.WITHDRAW,
    "bank_statement": BankOperationsInput.BANK_STATEMENT,
    "bankstatement": BankOperationsInput.BANK_STATEMENT,
    "bank statement": BankOperationsInput.BANK_STATEMENT
}

operations_pattern = r"bank[\s_]+statement|deposit|withdraw"
bank_statement_args_pattern = (
    r"(?P<operation_type>bank[\s_]+statement|deposit|withdraw)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<since>\d{4}[.-]\d\d\[.-]\d\d\)\s+"
    r"(?P<till>\d{4}[.-]\d\d\[.-]\d\d\)"
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
    # bank_statement_and_args2 := "  banKSTateMent  lolo dvosk  2050-12-12    1233.05.01",
    bank_statement_and_args3 := "bank_statement lolo   vosk  2014.12.01   2015-12-06",
    # input_bank_statement4 := " bank\nstatement",
]

for i in bank_statement_and_args:
    decomposite = re.search(bank_statement_args_pattern, i, flags=re.I)
    # print(operation.group(1))
    # print(dir(operation))

    # val = operation.group().lower()
    vals = decomposite.groups()
    # operation, first_name, last_name, amount = vals
    print(vals)
    # print(operation, first_name, last_name, amount)
    # get_op = operation_provider.get(val)
    # print(get_op)
    print(30 * "-")
