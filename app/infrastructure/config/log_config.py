from pathlib import Path

from pydantic_settings import BaseSettings

_BASE_DIR = Path(__file__).parent.parent.parent.parent
_LOGS_PATH = _BASE_DIR.joinpath("logs/", "operations_.txt")


class LogConfig(BaseSettings):
    """Log config"""

    LOG_FORMAT: str = "%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s"
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    NAME: str = "atm-banking.main"
    STREAM_LOG_LEVEL: str = "INFO"
    BASE_LEVEL: str = "INFO"
    FILE_LOG_LEVEL: str = "INFO"
    FILE_LOG_PATH: Path = _LOGS_PATH
    FILE_BACKUP_COUNT: int = 3


def get_log_config():
    return LogConfig()
