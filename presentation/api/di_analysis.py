import asyncio
import enum

from di.executors import AsyncExecutor
from di import Container, bind_by_type
from di.dependent import Dependent
from sqlalchemy.ext.asyncio import (AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker)

from infrastructure.unit_of_work import UnitOfWork
from infrastructure.database.core import create_engine, create_session_factory, create_db_session
from infrastructure.config.db_config import DBConfig
from infrastructure.database.repositories import (AccountRepo,
                                                  CustomerRepo,
                                                  OperationRepo,
                                                  IAccountRepo,
                                                  ICustomerRepo,
                                                  IOperationRepo)
from application.services import AccountService, CustomerService, OperationService
from application.usecases import BankStatement, Deposit, Withdraw, BaseUsecase


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
        Dependent(AccountRepo, scope=DIScope.REQUEST), IAccountRepo))
    container.bind(bind_by_type(
        Dependent(CustomerRepo, scope=DIScope.REQUEST), ICustomerRepo))
    container.bind(bind_by_type(
        Dependent(OperationRepo, scope=DIScope.REQUEST), IOperationRepo))

    # solved_uow = container.solve(
    #     Dependent(UnitOfWork, scope=DIScope.REQUEST),
    #     scopes=["app", "request"])
    # solved_account_service = container.solve(
    #     Dependent(AccountService, scope=DIScope.REQUEST),
    #     scopes=["app", "request"])
    # solved_customer_service = container.solve(
    #     Dependent(CustomerService, scope=DIScope.REQUEST),
    #     scopes=["app", "request"]
    # )
    # solved_operation_service = container.solve(
    #     Dependent(OperationService, scope=DIScope.REQUEST),
    #     scopes=["app", "request"]
    # )

    # solved_bank_statement_usecase = container.solve(
    #     Dependent(BankStatement, scope=DIScope.REQUEST),
    #     scopes=["app", "request"]
    # )

    async with container.enter_scope("app") as app_state:

        async with container.enter_scope("request", state=app_state) as request_state:

            bu_solved = container.solve(
                Dependent(BaseUsecase, scope=DIScope.REQUEST),
                scopes=["app", "request"]
            )
            base_usecase = await bu_solved.execute_async(
                executor=executor, state=request_state
            )
            assert isinstance(base_usecase, BaseUsecase)
            assert isinstance(base_usecase._operation_service, OperationService)
            assert isinstance(base_usecase.uow, UnitOfWork)
            assert isinstance(base_usecase._customer_service._uow, UnitOfWork)
            assert (base_usecase.uow
                    is base_usecase._customer_service._uow)

        print("SOME MAIN APP'S LOGIC")

        # async with container.enter_scope("request", state=app_state) as request_state:
        #
        #     uow = await solved_uow.execute_async(executor=executor, state=request_state, values={CustomValue: CustomValue(value="VALUE")})
        #     uow.hello()
        #     assert isinstance(uow, UnitOfWork)
        #     assert isinstance(uow.account_repo, AccountRepository)
        #     assert isinstance(uow.customer_repo, CustomerRepository)
        #     assert isinstance(uow.operation_repo, OperationRepository)
        #     print(uow._session)
        #     assert (uow._session is uow.account_repo._session)
        #     assert isinstance(uow._session, AsyncSession)
        #     print("done")

        print("ONE MORE MAIN APP'S LOGIC")

        # async with container.enter_scope("request", state=app_state) as request_state:
        #
        #     uow = await solved_uow.execute_async(executor=executor, state=request_state, values={CustomValue: CustomValue(value="VALUE123")})
        #     uow.hello()
        #     assert isinstance(uow, UnitOfWork)
        #     assert isinstance(uow.account_repo, AccountRepository)
        #     assert isinstance(uow.customer_repo, CustomerRepository)
        #     assert isinstance(uow.operation_repo, OperationRepository)
        #     print(uow._session)
        #     assert (uow._session is uow.account_repo._session)
        #     print("done")


asyncio.run(main())
