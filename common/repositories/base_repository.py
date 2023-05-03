from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar("T")
DBModel = TypeVar("DBModel")


class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    async def add(self, model: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, model_id: int) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, model: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, model_id: int) -> None:
        raise NotImplementedError
