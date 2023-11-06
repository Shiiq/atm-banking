from pprint import PrettyPrinter


class OutputHandler(PrettyPrinter):

    def __init__(self):
        super().__init__()

    def print(self, *args, **kwargs):
        super().pprint(*args, **kwargs)
