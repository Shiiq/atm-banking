import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from common.database.models.db import *
from common.database.models.dto import *
from common.database.models.constants import BankOperationsFromInput
from common.database.repositories import AccountRepository, CustomerRepository, OperationRepository
from common.services import AccountService, CustomerService, OperationService
from common.settings import settings
from common.unit_of_work import UnitOfWork
from common.usecases.deposit import Deposit


from cli.input_parser import InputParserService


def init_db_engine(db_url: str) -> AsyncEngine:
    db_engine = create_async_engine(url=db_url, echo=True, echo_pool=True)
    return db_engine


async def create_db(db_engine: AsyncEngine, base_model) -> None:
    """Drops the database if it already exists and creates a new one"""
    async with db_engine.begin() as connection:
        await connection.run_sync(base_model.metadata.drop_all)
        await connection.run_sync(base_model.metadata.create_all)


async def upload_test_data(s: AsyncSession):
    cus_1 = BankCustomerModel(first_name="John", last_name="Doe", bank_account=BankAccountModel())
    cus_2 = BankCustomerModel(first_name="Colin", last_name="Frolin", bank_account=BankAccountModel())
    cus_3 = BankCustomerModel(first_name="Moki", last_name="Roki", bank_account=BankAccountModel())
    s.add_all([cus_1, cus_2, cus_3])
    await s.commit()


async def main():
    engine = init_db_engine(db_url=settings.SQLITE_DATABASE_URL)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)

    async with session_factory() as session:
        # await upload_test_data(session)
        uow = UnitOfWork(session=session,
                         account_repo=AccountRepository,
                         customer_repo=CustomerRepository,
                         operation_repo=OperationRepository)
        deposit_usecase = Deposit(uow)
        data = DepositInput(
            customer=CustomerInput(first_name="Chuck",
                                   last_name="Buzz"),
            operation=OperationInput(type_=BankOperationsFromInput.DEPOSIT,
                                     amount=100500)
        )
        result = await deposit_usecase(data)
        print(result)
        # acc_cus = await session.execute(
        #     select(BankAccountModel)
        #     .where(BankAccountModel.id == 2)
        #     .options(joinedload(BankAccountModel.customer))
        # )
        # acc_cus = await session.execute(
        #     select(BankCustomerModel)
        #     .where(BankCustomerModel.bank_account_id == 2)
        #     .options(joinedload(BankCustomerModel.bank_account))
        # )
        # acc_cus = acc_cus.scalars().first()
        # check = BankCustomerRead.from_orm(acc_cus)
        # print(check)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
