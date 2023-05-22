from cli.constants import BankOperationsFromInput
# from common.database.models import *
from common.database.models.db import *
from common.database.models.dto import *


class InputParserService:

    # input data examples
    # "withdraw jake james 100500"
    # "deposit jake james 7000"
    # "bank_statement jake james 2023-01-01 2023-05-01"

    @staticmethod
    def parse_input(input_data: str) -> BankStatementInputDTO | DepositInputDTO | WithdrawInputDTO:
        operation, first_name, last_name, *args = input_data.strip().split()
        customer_dto = CustomerInputDTO(first_name=first_name.lower(),
                                        last_name=last_name.lower())

        if operation.lower() == BankOperationsFromInput.BANK_STATEMENT:
            since, till = args[0], args[1]
            return BankStatementInputDTO(customer=customer_dto,
                                         since=since,
                                         till=till)

        elif operation.lower() == BankOperationsFromInput.DEPOSIT:
            amount = args[0]
            return DepositInputDTO(customer=customer_dto,
                                   amount=amount)

        elif operation.lower() == BankOperationsFromInput.WITHDRAW:
            amount = args[0]
            return WithdrawInputDTO(customer=customer_dto,
                                    amount=amount)

        else:
            # TODO to fix
            raise Exception("Wrong operation")
