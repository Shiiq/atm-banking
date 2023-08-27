from pydantic_settings import BaseSettings


class LogConfig(BaseSettings):
    """Log config"""

    LOG_FORMAT: str = "%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s"
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    NAME: str = "atm-banking.main"
    STREAM_LOG_LEVEL: str = "ERROR"
    BASE_LEVEL: str = "INFO"
    FILE_LOG_LEVEL: str = "INFO"
    FILE_LOG_PATH: str = "./logs/operations.txt"


def get_log_config():
    return LogConfig()
