from typing import Callable

from di import bind_by_type, Container
from di.executors import AsyncExecutor
from di.dependent import Dependent

from sqlalchemy.ext.asyncio import (AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker)

from app.infrastructure.config.db_config import DBConfig
from app.infrastructure.database.core import create_engine, create_session_factory, create_db_session
from app.infrastructure.database.repositories import (AccountRepo,
                                                      CustomerRepo,
                                                      OperationRepo,
                                                      IAccountRepo,
                                                      ICustomerRepo,
                                                      IOperationRepo)
from .container import DIContainer, DIScope


def setup_db_dependencies(
        container: Container,
        db_config: Callable[..., DBConfig]
):

    container.bind(bind_by_type(
        Dependent(db_config, scope=DIScope.APP),
        DBConfig)
    )

    container.bind(bind_by_type(
        Dependent(create_engine, scope=DIScope.APP),
        AsyncEngine)
    )

    container.bind(bind_by_type(
        Dependent(create_session_factory, scope=DIScope.APP),
        async_sessionmaker[AsyncSession])
    )

    container.bind(bind_by_type(
        Dependent(create_db_session, scope=DIScope.REQUEST),
        AsyncSession)
    )

    container.bind(bind_by_type(
        Dependent(AccountRepo, scope=DIScope.REQUEST),
        IAccountRepo)
    )

    container.bind(bind_by_type(
        Dependent(CustomerRepo, scope=DIScope.REQUEST),
        ICustomerRepo)
    )

    container.bind(bind_by_type(
        Dependent(OperationRepo, scope=DIScope.REQUEST),
        IOperationRepo)
    )


def build_container(
        db_config: Callable[..., DBConfig]
) -> DIContainer:

    container = Container()
    executor = AsyncExecutor()
    scopes = (DIScope.APP, DIScope.REQUEST)

    setup_db_dependencies(container=container,
                          db_config=db_config)

    di_container = DIContainer(container=container,
                               executor=executor,
                               scopes=scopes)

    return di_container
