from typing import Protocol


class IAccountRepo(Protocol):

    async def create(self, account):
        ...

    async def get_by_id(self, account_id):
        ...

    async def update(self, account):
        ...
