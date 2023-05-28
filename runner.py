import asyncio
from datetime import datetime, date

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from infrastructure.database.models.constants import BankOperationsFromInput, BankOperationsToDB
from infrastructure.database.repositories import AccountRepository, CustomerRepository, OperationRepository
from infrastructure.database.models.db import BankAccountModel, BankCustomerModel, BankOperationModel
from infrastructure.database.models.dto import *
from application.settings import settings
from infrastructure.unit_of_work import UnitOfWork
from application.usecases.deposit import Deposit
from application.usecases.withdraw import Withdraw


def init_db_engine(db_url: str) -> AsyncEngine:
    db_engine = create_async_engine(url=db_url, echo=True, echo_pool=True)
    return db_engine


async def create_db(db_engine: AsyncEngine, base_model) -> None:
    """Drops the database if it already exists and creates a new one"""
    async with db_engine.begin() as connection:
        await connection.run_sync(base_model.metadata.drop_all)
        await connection.run_sync(base_model.metadata.create_all)


async def upload_data(s: AsyncSession):
    cus_1 = BankCustomerModel(first_name="John",
                              last_name="Doe",
                              bank_account=BankAccountModel())
    cus_2 = BankCustomerModel(first_name="Colin",
                              last_name="Frolin",
                              bank_account=BankAccountModel())
    cus_3 = BankCustomerModel(first_name="Moki",
                              last_name="Roki",
                              bank_account=BankAccountModel())
    s.add_all([cus_1, cus_2, cus_3])
    await s.flush()
    entries = []
    for i in range(1, 30):
        entries.append(
            BankOperationModel(amount=10000,
                               bank_account_id=1,
                               bank_customer_id=1,
                               bank_operation_type=BankOperationsToDB.DEPOSIT,
                               created_at=datetime(year=2023, month=5, day=i)))
    s.add_all(entries)
    await s.commit()


async def main():
    engine = init_db_engine(db_url=settings.SQLITE_DATABASE_URL)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)

    async with session_factory() as session:
        # await upload_data(session)
        uow = UnitOfWork(session=session,
                         account_repo=AccountRepository,
                         customer_repo=CustomerRepository,
                         operation_repo=OperationRepository)
        # deposit_usecase = Deposit(uow)
        # withdraw_usecase = Withdraw(uow)
        # d_data = DepositInput(
        #     customer=CustomerInput(first_name="Chuck",
        #                            last_name="Buzz"),
        #     operation=OperationInput(type_=BankOperationsFromInput.DEPOSIT,
        #                              amount=100500)
        # )
        # w_data = WithdrawInput(
        #     customer=CustomerInput(first_name="Chuck",
        #                            last_name="Buzz"),
        #     operation=OperationInput(type_=BankOperationsFromInput.WITHDRAW,
        #                              amount=100500)
        # )
        # result = await withdraw_usecase(w_data)
        # print(result)
        start = date(year=2023, month=4, day=1)
        end = date(year=2023, month=5, day=29)
        ops = await uow.operation_repo.get_by_date_interval(
            start_date=start, end_date=end
        )
        ops = [BankOperationRead.from_orm(op) for op in ops]
        print(len(ops))


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
