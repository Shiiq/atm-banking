from sqlalchemy.ext.asyncio import async_sessionmaker

from infrastructure.unit_of_work import UnitOfWork
from app.infrastructure.database import AccountRepository, CustomerRepository, OperationRepository
from presentation.cli.not_actual.input_parser import InputParserService
from presentation.cli.constants import EXITING_MESSAGE, WELCOME_MESSAGE, ExitCommand, BankOperationsFromInput


class CLIApp:

    db_session: async_sessionmaker
    input_parser: InputParserService

    def __init__(self, input_parser, db_session):
        self.input_parser = input_parser
        self.db_session = db_session

    async def run(self):
        print(WELCOME_MESSAGE)
        while True:
            data = input()
            if data.strip().lower() == ExitCommand.EXIT:
                print(EXITING_MESSAGE)
                break
            else:
                try:
                    parsed_data = self.input_parser.parse(data)
                except:
                    # WRONG OPERATION
                    print("wrong")
                else:
                    async with self.db_session() as session:
                        uow = UnitOfWork(session=session,
                                         account_repo=AccountRepository,
                                         customer_repo=CustomerRepository,
                                         operation_repo=OperationRepository)
                    if parsed_data.operation == BankOperationsFromInput.BANK_STATEMENT:
                        # result = await
                        pass
