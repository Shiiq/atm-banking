from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepo:

    def __init__(self, session: AsyncSession):
        self._session = session


class ProtocolRepo(Protocol):

    async def create(self, obj):
        ...

    async def get_by_id(self, obj_id):
        ...

    async def update(self, obj):
        ...

    async def delete(self, obj_id):
        ...
