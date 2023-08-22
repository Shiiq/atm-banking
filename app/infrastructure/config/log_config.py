from pydantic_settings import BaseSettings


class LogConfig(BaseSettings):
    """Log config"""

    NAME = "atm logger"
    LEVEL = ...
