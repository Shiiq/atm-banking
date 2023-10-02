from pathlib import Path

from pydantic_settings import BaseSettings

_BASE_DIR = Path(__file__).parent.parent.parent.parent
_LOGS_PATH = _BASE_DIR.joinpath("logs/", "operations.txt")


class LogConfig(BaseSettings):
    """Log config"""

    LOG_FORMAT: str = "%(asctime)s::%(levelname)s::%(name)s::%(message)s"
    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    BASE_LEVEL: str = "INFO"
    STREAM_LOG_LEVEL: str = "WARNING"
    FILE_LOG_LEVEL: str = "INFO"
    FILE_LOG_PATH: Path = _LOGS_PATH
    FILE_BACKUP_COUNT: int = 3


def get_log_config():
    return LogConfig()
