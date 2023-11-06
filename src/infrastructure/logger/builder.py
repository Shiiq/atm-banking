import logging
from logging import handlers

from .log_config import LoggingConfig


def setup_root_logger(log_config: LoggingConfig):

    logger = logging.getLogger()
    logger.setLevel(log_config.base_level)
    formatter = logging.Formatter(
        fmt=log_config.log_format,
        datefmt=log_config.datetime_format
    )

    # system logging
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=log_config.stream_log_level)
    stream_handler.setFormatter(fmt=formatter)

    # app logging
    file_handler = handlers.RotatingFileHandler(
        filename=log_config.file_log_path,
        backupCount=log_config.file_backup_count
    )
    file_handler.setLevel(level=log_config.file_log_level)
    file_handler.setFormatter(fmt=formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
