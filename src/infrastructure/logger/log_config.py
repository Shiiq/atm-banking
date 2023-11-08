from dataclasses import dataclass


@dataclass(frozen=True)
class LoggingConfig:
    """Logging config."""

    log_format: str = "%(asctime)s::%(levelname)s::%(name)s::%(message)s"
    datetime_format: str = "%Y-%m-%d %H:%M:%S"
    base_level: str = "INFO"
    stream_log_level: str = "WARNING"
    file_log_level: str = "INFO"
    file_log_path: str = "./logs/operations.txt"
    file_backup_count: int = 3
