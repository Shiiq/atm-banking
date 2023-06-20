from typing import Protocol


class ProtocolRepo(Protocol):

    async def create(self, obj):
        ...

    async def get_by_id(self, obj_id):
        ...

    async def update(self, obj):
        ...


class ProtocolReader(Protocol):

    pass
