

class ApplicationException(Exception):
    """Base class for application exception"""

    @property
    def msg(self):
        ...

    pass
