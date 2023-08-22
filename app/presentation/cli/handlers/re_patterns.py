import re

_operation_types_pattern = r"bank[\s_]?statement|deposit|withdraw|exit"
OPERATION_TYPES_PATTERN = re.compile(_operation_types_pattern)

_bank_statement_operation_pattern = (
    r"(?P<operation_type>bank[\s_]?statement)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<since>(\d{2})[.-](\d{2})[.-](\d{4}))\s+"
    r"(?P<till>(\d{2})[.-](\d{2})[.-](\d{4}))"
)
BANK_STATEMENT_OPERATION_PATTERN = re.compile(_bank_statement_operation_pattern)

_deposit_operation_pattern = (
    r"(?P<operation_type>deposit)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<amount>\d{1,7})"
)
DEPOSIT_OPERATION_PATTERN = re.compile(_deposit_operation_pattern)

_withdraw_operation_pattern = (
    r"(?P<operation_type>withdraw)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<amount>\d{1,7})"
)
WITHDRAW_OPERATION_PATTERN = re.compile(_withdraw_operation_pattern)

_bank_statement_variations_pattern = r"bank[\s_]?statement"
BANK_STATEMENT_VARIATIONS_PATTERN = re.compile(_bank_statement_variations_pattern)
REPL_BANK_STATEMENT_PATTERN = r"bank_statement"

_date_variations_pattern = r"(\d{2})[.-](\d{2})[.-](\d{4})"
DATE_VARIATIONS_PATTERN = re.compile(_date_variations_pattern)
REPL_DATE_PATTERN = r"\3-\2-\1"

__all__ = (
    "OPERATION_TYPES_PATTERN",
    "BANK_STATEMENT_OPERATION_PATTERN",
    "DEPOSIT_OPERATION_PATTERN",
    "WITHDRAW_OPERATION_PATTERN",
    "BANK_STATEMENT_VARIATIONS_PATTERN",
    "REPL_BANK_STATEMENT_PATTERN",
    "DATE_VARIATIONS_PATTERN",
    "REPL_DATE_PATTERN",
)
