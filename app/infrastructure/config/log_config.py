from pydantic_settings import BaseSettings


class LogConfig(BaseSettings):
    """Log config"""

    LOG_FORMAT: str = "%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s"
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    NAME: str = "app"
    LEVEL: str = "INFO"


def get_log_config():
    return LogConfig()
