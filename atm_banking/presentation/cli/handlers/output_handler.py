from atm_banking.application.dto import BankStatementShortResponse
from atm_banking.application.dto import OperationShortResponse


class OutputHandler:

    def print(
            self,
            data: str | BankStatementShortResponse | OperationShortResponse
    ):

        # if we get BankStatementShortResponse or OperationShortResponse,
        # we need to parse it to form an output message
        if isinstance(data, BankStatementShortResponse):
            print(self.get_bankstatement_info_msg(data))
        elif isinstance(data, OperationShortResponse):
            print(self.get_operation_info_msg(data))
        # but if we get as data a simple string
        # e.g. exception message or operational message,
        # we print it directly
        elif isinstance(data, str):
            print(data)

    def get_operation_info_msg(
            self,
            operation_data: OperationShortResponse
    ) -> str:

        msg = 55 * "="
        msg += self._render_operation_msg(operation_data)
        msg += (
            "| current balance | {current_balance:<33,} |"
            "\n"
            .format(current_balance=operation_data.current_balance)
        )
        msg += 55 * "="
        return msg

    def get_bankstatement_info_msg(
            self,
            operation_data: BankStatementShortResponse
    ) -> str:

        header = 55 * "="
        header += (
            "\n"
            "| since           | {since!s:<33} |"
            "\n"
            "| till            | {till!s:<33} |"
            "\n"
            "| current balance | {current_balance:<33,} |"
            "\n"
            .format(
                since=operation_data.since,
                till=operation_data.till,
                current_balance=operation_data.current_balance
            )
        )
        body = 55 * "="
        if not operation_data.operations:
            body += (
                "\n"
                f"| {'There arent operations for the specified period':^51} |"
                "\n"
            )
        else:
            for op in operation_data.operations:
                body += self._render_operation_msg(op)
        body += 55 * "="
        return header+body

    def _render_operation_msg(
            self,
            data: BankStatementShortResponse | OperationShortResponse
    ) -> str:

        msg = (
            "\n"
            "| date            | {date!s:<33} |"
            "\n"
            "| operation       | {operation:<33} |"
            "\n"
            "| amount          | {amount:<33,} |"
            "\n"
            .format(
                date=data.created_at,
                operation=data.bank_operation_type,
                amount=data.amount,
            )
        )
        return msg
