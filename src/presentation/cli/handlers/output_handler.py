from pprint import PrettyPrinter


class OutputHandler(PrettyPrinter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print(self, *args, **kwargs):
        super().pprint(*args, **kwargs)
