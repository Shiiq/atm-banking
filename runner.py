import asyncio
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from common.database.models import *
from common.database.repositories import AccountRepository, CustomerRepository
from common.settings import settings
from common.unit_of_work import UnitOfWork


def init_db_engine(db_url: str) -> AsyncEngine:
    db_engine = create_async_engine(url=db_url, echo=True, echo_pool=True)
    return db_engine


async def create_db(db_engine: AsyncEngine, base_model) -> None:
    """Drops the database if it already exists and creates a new one"""
    async with db_engine.begin() as connection:
        await connection.run_sync(base_model.metadata.drop_all)
        await connection.run_sync(base_model.metadata.create_all)


async def main():
    engine = init_db_engine(db_url=settings.SQLITE_DATABASE_URL)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

    async with session_factory() as session:
        uow = UnitOfWork(session=session,
                         account_repo=AccountRepository,
                         customer_repo=CustomerRepository)

        async def upload_test_data(s: AsyncSession):
            cus_1 = BankCustomerModel(first_name="John", last_name="Doe", bank_account=BankAccountModel())
            cus_2 = BankCustomerModel(first_name="Colin", last_name="Frolin", bank_account=BankAccountModel())
            cus_3 = BankCustomerModel(first_name="Moki", last_name="Roki", bank_account=BankAccountModel())
            s.add_all([cus_1, cus_2, cus_3])
            await s.commit()
        # await upload_test_data(session)
        dt = datetime(2023, 5, 12)
        query = (select(BankCustomerModel).where(BankCustomerModel.created_at >= dt))
        cuss = await session.execute(query)
        cuss = cuss.scalars().all()
        print(*cuss)
        # c = CustomerDTO(first_name="Peter", last_name="Shmiter")
        # c_service = AltCustomerService(customer_dto=c, uow=uow)
        # await c_service.customer_create()
        # new_c = await c_service.customer_by_id(customer_id=3)
        # print("\n", new_c, "\n")


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
