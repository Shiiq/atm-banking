import asyncio
from datetime import datetime
from pprint import pprint

from sqlalchemy import inspect, select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from infrastructure.config.db_config import get_db_config
from infrastructure.database.models.constants import BankOperationsToDB
from infrastructure.database.models.db import BankCustomerModel, BankOperationModel


def init_db_engine(db_url: str) -> AsyncEngine:
    db_engine = create_async_engine(url=db_url, echo=False, echo_pool=True)
    return db_engine


async def create_db(db_engine: AsyncEngine, base_model) -> None:
    """Drops the database if it already exists and creates a new one"""
    async with db_engine.begin() as connection:
        await connection.run_sync(base_model.metadata.drop_all)
        await connection.run_sync(base_model.metadata.create_all)


async def upload_data(s: AsyncSession):
    # cus_1 = BankCustomerModel(first_name="john",
    #                           last_name="doe",
    #                           bank_account=BankAccountModel())
    # cus_2 = BankCustomerModel(first_name="colin",
    #                           last_name="frolin",
    #                           bank_account=BankAccountModel())
    # cus_3 = BankCustomerModel(first_name="moki",
    #                           last_name="roki",
    #                           bank_account=BankAccountModel())
    # s.add_all([cus_1, cus_2, cus_3])
    await s.flush()
    entries = []
    for i in range(1, 4):
        entries.append(
            BankOperationModel(amount=10000,
                               bank_account_id=1,
                               bank_customer_id=1,
                               bank_operation_type=BankOperationsToDB.DEPOSIT,
                               created_at=datetime.now()))
    s.add_all(entries)
    await s.commit()


def get_state_of_obj(obj):
    print(f"transient - {inspect(obj).transient} | "
          f"pending - {inspect(obj).pending} | "
          f"persistent - {inspect(obj).persistent} | "
          f"deleted - {inspect(obj).deleted} | "
          f"detached - {inspect(obj).detached}")


async def main():
    config = get_db_config()
    engine = init_db_engine(db_url=config.sqlite_url)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)

    async with session_factory() as session:
        # await upload_data(session)
        query = select(BankCustomerModel).where(BankCustomerModel.id == 1)
        res = await session.execute(query)
        result = res.scalars().first()
        # query = select(BankCustomerModel).where(BankCustomerModel.id == 1).exists()
        # query = (update(BankCustomerModel)
        #          .where(BankCustomerModel.id == 1)
        #          .values(first_name="john"))

        # s_data = dto.BankStatementInput(first_name="JoHN",
        #                                 last_name="dOe",
        #                                 since=date(year=2023, month=6, day=28),
        #                                 till=date(year=2023, month=6, day=29))
        # result = await statement_usecase(s_data)
        # d_data = dto.DepositInput(first_name="JoHN",
        #                           last_name="dOe",
        #                           amount=100500)
        # result = await deposit_usecase(d_data)
        # w_data = dto.WithdrawInput(first_name="JoHN",
        #                            last_name="dOe",
        #                            amount=100500)
        # result = await withdraw_usecase(w_data)
        pprint(result)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
