

OPERATION_TYPES_PATTERN = r"bank[\s_]?statement|deposit|withdraw|exit"

BANK_STATEMENT_OPERATION_PATTERN = (
    r"(?P<operation_type>bank[\s_]?statement)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<since>(\d{4})[.-](\d{2})[.-](\d{2}))\s+"
    r"(?P<till>(\d{4})[.-](\d{2})[.-](\d{2}))"
)

DEPOSIT_OPERATION_PATTERN = (
    r"(?P<operation_type>deposit)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<amount>\d{1,7})"
)

WITHDRAW_OPERATION_PATTERN = (
    r"(?P<operation_type>withdraw)\s+"
    r"(?P<first_name>[^\W\d]+)\s+"
    r"(?P<last_name>[^\W\d]+)\s+"
    r"(?P<amount>\d{1,7})"
)

BANK_STATEMENT_VARIATIONS_PATTERN = r"bank[\s_]?statement"
REPL_BANK_STATEMENT_PATTERN = r"bank_statement"
DATE_VARIATIONS_PATTERN = r"(\d{4})[.-](\d{2})[.-](\d{2})"
REPL_DATE_PATTERN = r"\1-\2-\3"
