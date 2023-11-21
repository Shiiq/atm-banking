from pprint import PrettyPrinter

from src.application.dto import BankStatementShortResponse
from src.application.dto import OperationShortResponse


class OutputHandler(PrettyPrinter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _print(self, *args, **kwargs):
        super().pprint(*args, **kwargs)

    def print(self, data):
        print(55 * "=")
        if isinstance(data, BankStatementShortResponse):
            print(self.get_bankstatement_info_msg(data))
        elif isinstance(data, OperationShortResponse):
            print(self.get_operation_info_msg(data))
        print(55 * "=")

    def get_operation_info_msg(
            self,
            operation_data: OperationShortResponse
    ) -> str:
        msg = (
            "| date            | {date!s:<33} |"
            "\n"
            "| operation       | {operation:<33} |"
            "\n"
            "| amount          | {amount:<33,} |"
            "\n"
            "| current balance | {current_balance:<33,} |"
            .format(
                date=operation_data.created_at,
                operation=operation_data.bank_operation_type,
                amount=operation_data.amount,
                current_balance=operation_data.current_balance
            )
        )
        return msg

    def get_bankstatement_info_msg(
            self,
            operation_data: BankStatementShortResponse
    ) -> str:
        header = (
            "| since           | {since!s:<33} |"
            "\n"
            "| till            | {till!s:<33} |"
            "\n"
            "| current balance | {current_balance:<33,} |"
            .format(
                since=operation_data.since,
                till=operation_data.till,
                current_balance=operation_data.current_balance
            )
        )
        if not operation_data.operations:
            body = "\n| There aren't operations for the specified period |"
        else:
            body = ""
            for o in operation_data.operations:
                body += self.get_operation_info_msg(o)
                body += 55 * "="
        return header+body
