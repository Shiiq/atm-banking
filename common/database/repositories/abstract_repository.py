from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

DBModel = TypeVar("DBModel")


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
