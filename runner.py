import asyncio
import sys
import logging

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from common.database.models import *
from common.database.repositories import AccountRepository, CustomerRepository
from common.settings import settings
from common.uow import UnitOfWork

from cli.input_parser import InputParserService


def init_db_engine(db_url: str) -> AsyncEngine:
    db_engine = create_async_engine(url=db_url, echo=True, echo_pool=True)
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

        customer_dto_1 = CustomerBaseDTO(first_name="john", last_name="jakes")
        customer_dto_2 = CustomerBaseDTO(first_name="akoz", last_name="pors")
        account_dto = AccountBaseDTO()

        # CUSTOMER AND ACCOUNT THROUGH ACCOUNT
        # account_orm = BankAccountModel(**account_dto.dict(),
        #                                customer=BankCustomerModel(**customer_dto_1.dict()))
        # account_from_db = await uow.account_repo.add(account_orm)
        # print(account_from_db.id, account_from_db.customer.id)

        # CUSTOMER AND ACCOUNT THROUGH CUSTOMER
        customer_orm = BankCustomerModel(**customer_dto_2.dict(),
                                         bank_account=BankAccountModel(**account_dto.dict()))
        # customer_from_db = await uow.customer_repo.add(customer_orm)
        # print(customer_from_db.id, customer_from_db.bank_account_id)
        # await uow.commit()
        c = await uow.customer_repo.get_by_id(customer_id=1)
        print(c.bank_account_id)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
