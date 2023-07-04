import asyncio
import enum

from di.executors import AsyncExecutor
from di.api.scopes import Scope
from di import Container, ScopeState, bind_by_type
from di.dependent import Dependent
from di.api.providers import DependencyProvider, DependencyProviderType
from sqlalchemy.ext.asyncio import (AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker)

from infrastructure.unit_of_work import UnitOfWork, CustomValue
from infrastructure.database.db_core import create_engine, create_session_factory, create_db_session
from infrastructure.database.db_config import DBConfig
from infrastructure.database.repositories import (AccountRepository,
                                                  CustomerRepository,
                                                  OperationRepository,
                                                  IAccountRepo,
                                                  ICustomerRepo,
                                                  IOperationRepo)


class DIScope(enum.StrEnum):
    APP = "app"
    REQUEST = "request"


async def main():

    # stubs
    def get_config():
        return DBConfig()
    # def get_session():
    #     return "stub_session"
    # container.bind(bind_by_type(
    #     Dependent(get_session, scope=DIScope.APP), AsyncSession))

    container = Container()
    executor = AsyncExecutor()

    container.bind(bind_by_type(
        Dependent(get_config, scope=DIScope.APP), DBConfig))
    container.bind(bind_by_type(
        Dependent(create_engine, scope=DIScope.APP), AsyncEngine))
    container.bind(bind_by_type(
        Dependent(create_session_factory, scope=DIScope.APP), async_sessionmaker[AsyncSession]))
    container.bind(bind_by_type(
        Dependent(create_db_session, scope=DIScope.REQUEST), AsyncSession))
    container.bind(bind_by_type(
        Dependent(AccountRepository, scope=DIScope.REQUEST), IAccountRepo))
    container.bind(bind_by_type(
        Dependent(CustomerRepository, scope=DIScope.REQUEST), ICustomerRepo))
    container.bind(bind_by_type(
        Dependent(OperationRepository, scope=DIScope.REQUEST), IOperationRepo))

    solved_uow = container.solve(Dependent(UnitOfWork, scope=DIScope.REQUEST), scopes=["app", "request"])

    async with container.enter_scope("app") as app_state:

        print("SOME MAIN APP'S LOGIC")

        async with container.enter_scope("request", state=app_state) as request_state:

            uow = await solved_uow.execute_async(executor=executor, state=request_state, values={CustomValue: CustomValue(value="VALUE")})
            uow.hello()
            assert isinstance(uow, UnitOfWork)
            assert isinstance(uow.account_repo, AccountRepository)
            assert isinstance(uow.customer_repo, CustomerRepository)
            assert isinstance(uow.operation_repo, OperationRepository)
            print(uow._session)
            assert (uow._session is uow.account_repo._session)
            assert isinstance(uow._session, AsyncSession)
            print("done")

        print("ONE MORE MAIN APP'S LOGIC")

        async with container.enter_scope("request", state=app_state) as request_state:

            uow = await solved_uow.execute_async(executor=executor, state=request_state, values={CustomValue: CustomValue(value="VALUE123")})
            uow.hello()
            assert isinstance(uow, UnitOfWork)
            assert isinstance(uow.account_repo, AccountRepository)
            assert isinstance(uow.customer_repo, CustomerRepository)
            assert isinstance(uow.operation_repo, OperationRepository)
            print(uow._session)
            assert (uow._session is uow.account_repo._session)
            print("done")


asyncio.run(main())
