import logging
from logging import handlers

from src.infrastructure.config.alter_log_config import LogConfig


def setup_root_logger(log_config: LogConfig):

    logger = logging.getLogger()
    logger.setLevel(log_config.BASE_LEVEL)
    formatter = logging.Formatter(
        fmt=log_config.LOG_FORMAT,
        datefmt=log_config.DATETIME_FORMAT
    )

    # system logging
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=log_config.STREAM_LOG_LEVEL)
    stream_handler.setFormatter(fmt=formatter)

    # app logging
    file_handler = handlers.RotatingFileHandler(
        filename=log_config.FILE_LOG_PATH,
    )
    file_handler.setLevel(level=log_config.FILE_LOG_LEVEL)
    file_handler.setFormatter(fmt=formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
