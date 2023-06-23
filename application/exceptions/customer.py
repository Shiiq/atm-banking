

class CustomerIDNotExist(Exception):

    def __init__(self, obj_id: int):
        self.obj_id = obj_id

    @property
    def message(self):
        return f"A customer with ID '{self.obj_id}' does not exist"


class CustomerNotExist(Exception):

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def message(self):
        return f"A customer '{self._fullname}' does not exist"

    @property
    def _fullname(self):
        return f"{self.first_name} {self.last_name}"
