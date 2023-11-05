from di import bind_by_type, Container
from di.dependent import Dependent
from di.executors import AsyncExecutor
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.application.interfaces import IAccountRepo
from src.application.interfaces import ICustomerRepo
from src.application.interfaces import IOperationRepo
from src.application.interfaces import IUnitOfWork
from src.infrastructure.config.db_config import DBConfig
from src.infrastructure.database.core import create_engine
from src.infrastructure.database.core import create_engine_local_way
from src.infrastructure.database.core import create_db_session
from src.infrastructure.database.core import create_session_factory
from src.infrastructure.database.models import Base
from src.infrastructure.database.repositories import AccountRepo
from src.infrastructure.database.repositories import CustomerRepo
from src.infrastructure.database.repositories import OperationRepo
from src.infrastructure.di import DIContainer, DIScope
from src.infrastructure.unit_of_work import UnitOfWork


def setup_db_dependencies(container: Container, db_config: DBConfig):

    container.bind(bind_by_type(
        Dependent(lambda *args: db_config, scope=DIScope.APP), DBConfig)
    )
    if db_config.local:
        container.bind(bind_by_type(
            Dependent(lambda *args: Base.metadata, scope=DIScope.APP), MetaData)
        )
        container.bind(bind_by_type(
            Dependent(create_engine_local_way, scope=DIScope.APP), AsyncEngine)
        )
    else:
        container.bind(bind_by_type(
            Dependent(create_engine, scope=DIScope.APP), AsyncEngine)
        )
    container.bind(bind_by_type(
        Dependent(create_session_factory, scope=DIScope.APP), async_sessionmaker)
    )
    container.bind(bind_by_type(
        Dependent(create_db_session, scope=DIScope.REQUEST), AsyncSession)
    )

    container.bind(bind_by_type(
        Dependent(UnitOfWork, scope=DIScope.REQUEST), IUnitOfWork)
    )
    container.bind(bind_by_type(
        Dependent(AccountRepo, scope=DIScope.REQUEST), IAccountRepo)
    )
    container.bind(bind_by_type(
        Dependent(CustomerRepo, scope=DIScope.REQUEST), ICustomerRepo)
    )
    container.bind(bind_by_type(
        Dependent(OperationRepo, scope=DIScope.REQUEST), IOperationRepo)
    )


def build_container(db_config: DBConfig) -> DIContainer:

    container = Container()
    executor = AsyncExecutor()
    scopes = (DIScope.APP, DIScope.REQUEST)

    setup_db_dependencies(container=container, db_config=db_config)
    di_container = DIContainer(
        container=container,
        executor=executor,
        scopes=scopes
    )
    return di_container
