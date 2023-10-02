

class ApplicationException(Exception):
    """Base class for application exception"""

    msg: str
    ui_msg: str
