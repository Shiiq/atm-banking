from .base import ApplicationException


class CustomerIDNotExist(ApplicationException):

    def __init__(self, customer_id: int):
        self.customer_id = customer_id

    @property
    def msg(self):
        return f"A customer with ID '{self.customer_id}' does not exist"

    def __str__(self):
        return self.msg


class CustomerNotExist(ApplicationException):

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def msg(self):
        return f"A customer '{self._fullname()}' does not exist"

    def _fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.msg
