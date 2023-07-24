

class WrongOperationError(Exception):

    def __init__(self, d):
        self.d = d

    @property
    def message(self):
        return f"{self.d}"

    def __str__(self):
        return self.message


class ExitOperation(Exception):

    def __init__(self, d):
        self.d = d

    @property
    def message(self):
        return f"{self.d}"

    def __str__(self):
        return self.message
