from typing import Protocol


class IAccountRepo(Protocol):

    async def create(self, account):
        ...

    async def get_by_id(self, account_id):
        ...

    async def update(self, account):
        ...


class ICustomerRepo(Protocol):

    async def create(self, customer):
        ...

    async def get_by_id(self, customer_id):
        ...

    async def get_by_fullname(self, customer_first_name, customer_last_name):
        ...


class IOperationRepo(Protocol):

    async def create(self, operation):
        ...

    async def get_all(self):
        ...

    async def get_by_id(self, operation_id):
        ...

    async def get_by_account_id(self, account_id):
        ...

    async def get_by_customer_id(self, customer_id):
        ...

    async def get_by_date_interval(self, account_id, customer_id, start_date, end_date):
        ...
