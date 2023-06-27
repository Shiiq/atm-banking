import asyncio
from datetime import datetime

from sqlalchemy import inspect, select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from infrastructure.database.models.constants import BankOperationsFromInput, BankOperationsToDB
from infrastructure.database.repositories import AccountRepository, CustomerRepository, OperationRepository
from infrastructure.database.models.db import BankAccountModel, BankCustomerModel, BankOperationModel
from infrastructure.database.models import dto
from application.settings import settings
from infrastructure.unit_of_work import UnitOfWork
from application.usecases import BankStatement, Deposit, Withdraw



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
                               created_at=datetime(year=2023, month=5, day=i, hour=12)))
    s.add_all(entries)
    await s.commit()


def get_state_of_obj(obj):
    print(f"transient - {inspect(obj).transient} | "
          f"pending - {inspect(obj).pending} | "
          f"persistent - {inspect(obj).persistent} | "
          f"deleted - {inspect(obj).deleted} | "
          f"detached - {inspect(obj).detached}")


async def main():
    engine = init_db_engine(db_url=settings.SQLITE_DATABASE_URL)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)

    async with session_factory() as session:
        # await upload_data(session)
        uow = UnitOfWork(session=session,
                         account_repo=AccountRepository,
                         customer_repo=CustomerRepository,
                         operation_repo=OperationRepository)

        # query = select(BankCustomerModel).where(BankCustomerModel.id == 1).exists()
        # res = await session.execute(select(query))
        # print(res.scalar())
        # statement_usecase = BankStatement(uow=uow)
        deposit_usecase = Deposit(uow)
        withdraw_usecase = Withdraw(uow)
        # s_data = dto.BankStatementInput(
        #     customer=dto.CustomerInput(first_name="JoHN",
        #                                last_name="dOe"),
        #     operation=dto.OperationInput(type_=BankOperationsFromInput.BANK_STATEMENT,
        #                                  since=datetime(year=2023, month=5, day=1),
        #                                  till=datetime(year=2023, month=5, day=15))
        # )
        # result = await statement_usecase(s_data)
        # d_data = dto.DepositInput(
        #     customer=dto.CustomerInput(first_name="Chuck",
        #                                last_name="Buzz"),
        #     operation=dto.OperationInput(type_=BankOperationsFromInput.DEPOSIT,
        #                                  amount=100500))
        # result = await deposit_usecase(d_data)
        w_data = dto.WithdrawInput(
            customer=dto.CustomerInput(first_name="Chuck",
                                       last_name="Buzz"),
            operation=dto.OperationInput(type_=BankOperationsFromInput.WITHDRAW,
                                         amount=100500)
        )
        result = await withdraw_usecase(w_data)
        print(result or None)



if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
