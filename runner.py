import sys
import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from common.database.models import *
from common.database.repositories import AccountRepository, CustomerRepository
from common.settings import settings
from common.uow import UnitOfWork

from cli.input_parser import InputParserService


def init_db_engine(db_url: str) -> AsyncEngine:
    db_engine = create_async_engine(url=db_url, echo=False)
    return db_engine


async def create_db(db_engine: AsyncEngine, base_model) -> None:
    """Drops the database if it already exists and creates a new one"""
    async with db_engine.begin() as connection:
        await connection.run_sync(base_model.metadata.drop_all)
        await connection.run_sync(base_model.metadata.create_all)


def send_message_to_stdout(message: str) -> None:
    """Writes message to the stdout stream"""
    sys.stdout.write(message)


async def main():
    engine = init_db_engine(db_url=settings.SQLITE_DATABASE_URL)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)
    # input_data = input("please input --->  ")
    # print(InputParserService.parse_input(input_data))
    # output_data = InputParserService.parse_input(input_data)
    async with session_factory() as session:

        uow = UnitOfWork(session=session,
                         account_repo=AccountRepository,
                         customer_repo=CustomerRepository)
        # acc = BankAccountModel(deposit=1000)
        # cus = BankCustomerModel(first_name="john",
        #                         last_name="jakes",
        #                         bank_account=acc)
        cus_dto_in = BankCustomerBaseDTO(first_name="john", last_name="jakes")
        cus_dto_to_db = BankCustomerToDB(**cus_dto_in.dict())
        cus_orm_to_db = BankCustomerModel(**cus_dto_to_db.dict())
        cus_new = await uow.customer_repo.add(cus_orm_to_db)
        # acc = await uow.account_repo.add(acc)
        await uow.commit()


if __name__ == "__main__":
    asyncio.run(main())
