import sys
import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from common.database.models.db_models import BankAccountModel, BankClientModel
from common.settings import settings


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

from common.database.repository import BankClientRepository
async def main():
    engine = init_db_engine(db_url=settings.SQLITE_DATABASE_URL)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with session_factory() as session:
        acc = BankAccountModel(deposit=1000)
        cli = BankClientModel(first_name="john",
                              last_name="jakes",
                              bank_account=acc)
        session.add_all([acc, cli])
        await session.commit()

        r = BankClientRepository()
        from common.database.models.dto_models import DepositOrWithdrawDTO
        d = DepositOrWithdrawDTO(
            first_name="john",
            last_name="jakes",
            operation="deposit",
            amount=1500
        )
        # c = await r.get_or_none(s=session, data=d)
        # print()


    # await create_db(db_engine=engine, base_model=BaseModel)
    # send_message_to_stdout(WELCOME_MESSAGE)
    # while True:
    #     input_args = input("request >>>  ")
    #     if input_args.strip().lower() == ExitCommand.EXIT:
    #         send_message_to_stdout(EXITING_MESSAGE)
    #         break
    #     else:
    #         data = parse_args(input_args)
    #         print(data)
    # sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
