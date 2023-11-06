from dataclasses import dataclass
from pathlib import Path

_BASE_DIR = Path(__file__).parent.parent.parent.parent
_LOGS_PATH = _BASE_DIR.joinpath("logs/", "operations.txt")


@dataclass(frozen=True)
class LoggingConfig:
    """Log config"""

    log_format: str = "%(asctime)s::%(levelname)s::%(name)s::%(message)s"
    datetime_format: str = "%Y-%m-%d %H:%M:%S"
    base_level: str = "INFO"
    stream_log_level: str = "WARNING"
    file_log_level: str = "INFO"
    file_log_path: str = "./logs/operations.txt"
    file_backup_count: int = 3
