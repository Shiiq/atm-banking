from abc import ABC, abstractmethod
from typing import Generic, Optional, Protocol, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

DBModel = TypeVar("DBModel")


class ConnHolder:

    def __init__(self, session: AsyncSession):
        self._session = session


class ProtocolRepository(Protocol):

    async def add(self, model):
        ...

    async def get_by_id(self, model_id):
        ...

    async def update(self, model):
        ...

    async def delete(self, model_id):
        ...


class AbstractRepository(ABC, Generic[DBModel]):

    @abstractmethod
    async def add(self, model: DBModel) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, model_id: int) -> Optional[DBModel]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, model: DBModel) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, model_id: int) -> None:
        raise NotImplementedError
