from typing import Callable

from di import bind_by_type, Container
from di.executors import AsyncExecutor
from di.dependent import Dependent, JoinedDependent
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

# from src.infrastructure.config.db_config import DBConfig
from src.infrastructure.config.alter_db_config import DBConfig
from src.infrastructure.database.core import create_engine
from src.infrastructure.database.core import create_db_session
from src.infrastructure.database.core import create_session_factory
from src.infrastructure.database.core import make_migrations
from src.infrastructure.database.models import Base
from src.infrastructure.database.repositories import AccountRepo
from src.infrastructure.database.repositories import CustomerRepo
from src.infrastructure.database.repositories import OperationRepo
from src.infrastructure.database.repositories import IAccountRepo
from src.infrastructure.database.repositories import ICustomerRepo
from src.infrastructure.database.repositories import IOperationRepo

from .container import DIContainer, DIScope


def setup_db_dependencies(
        container: Container,
        db_config: Callable[..., DBConfig],
        # db_config: DBConfig
):

    # container.bind(bind_by_type(
    #     Dependent(lambda *args: db_config, scope=DIScope.APP),
    #     DBConfig
    # ))
    container.bind(bind_by_type(
        Dependent(db_config, scope=DIScope.APP),
        DBConfig
    ))
    container.bind(bind_by_type(
        Dependent(create_engine, scope=DIScope.APP),
        AsyncEngine
    ))

    # if db_config.LOCAL:
    #     print("DB_CONFIG LOCAAAAAAAAAAAL")
    # container.bind(bind_by_type(
    #     Dependent(lambda *args: Base.metadata, scope=DIScope.APP),
    #     MetaData
    # ))
        # mig = JoinedDependent(
        #     Dependent(make_migrations, scope=DIScope.APP),
        #     siblings=[Dependent(create_engine, scope=DIScope.APP)]
        # )
        # container.bind(lambda *args: mig)
    container.bind(lambda *args: Dependent(make_migrations, scope=DIScope.APP))
        # container.solve(
        #     Dependent(make_migrations, scope=DIScope.APP),
        #     scopes=[DIScope.APP, DIScope.REQUEST]
        # )

    container.bind(bind_by_type(
        Dependent(create_session_factory, scope=DIScope.APP),
        async_sessionmaker[AsyncSession]
    ))

    container.bind(bind_by_type(
        Dependent(create_db_session, scope=DIScope.REQUEST),
        AsyncSession
    ))

    container.bind(bind_by_type(
        Dependent(AccountRepo, scope=DIScope.REQUEST),
        IAccountRepo
    ))

    container.bind(bind_by_type(
        Dependent(CustomerRepo, scope=DIScope.REQUEST),
        ICustomerRepo
    ))

    container.bind(bind_by_type(
        Dependent(OperationRepo, scope=DIScope.REQUEST),
        IOperationRepo
    ))


def build_container(
        db_config: Callable[..., DBConfig]
        # db_config: DBConfig
) -> DIContainer:

    container = Container()
    executor = AsyncExecutor()
    scopes = (DIScope.APP, DIScope.REQUEST)

    setup_db_dependencies(
        container=container,
        db_config=db_config
    )
    di_container = DIContainer(
        container=container,
        executor=executor,
        scopes=scopes
    )

    return di_container
