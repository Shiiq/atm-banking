from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar


ConnObj = TypeVar("ConnObj")


class BaseConnection(ABC, Generic[ConnObj]):

    @abstractmethod
    async def commit(self, session: ConnObj) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self, session: ConnObj) -> None:
        raise NotImplementedError
