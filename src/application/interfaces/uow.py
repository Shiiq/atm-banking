from typing import Protocol


class IUnitOfWork(Protocol):

    async def commit(self):
        ...

    async def rollback(self):
        ...
