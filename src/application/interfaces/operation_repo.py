from typing import Protocol


class IOperationRepo(Protocol):

    async def create(self, operation):
        ...

    async def get_all(self):
        ...

    async def get_by_id(self, operation_id):
        ...

    async def get_by_customer_id(self, account_id, customer_id):
        ...

    async def get_by_date_interval(self, account_id, customer_id, start_date, end_date):
        ...
