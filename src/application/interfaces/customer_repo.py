from typing import Protocol


class ICustomerRepo(Protocol):

    async def create(self, customer):
        ...

    async def get_by_id(self, customer_id):
        ...

    async def get_by_fullname(self, customer_first_name, customer_last_name):
        ...
