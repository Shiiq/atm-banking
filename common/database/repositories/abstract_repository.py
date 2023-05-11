from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession


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
