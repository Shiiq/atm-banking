import logging
from logging import Logger, handlers

from app.infrastructure.config.log_config import LogConfig


def build_main_logger(log_config: LogConfig):
    logger = logging.getLogger()
    logger.setLevel(log_config.BASE_LEVEL)
    formatter = logging.Formatter(
        fmt=log_config.LOG_FORMAT,
        datefmt=log_config.DATE_FORMAT
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=log_config.STREAM_LOG_LEVEL)
    stream_handler.setFormatter(fmt=formatter)

    file_handler = handlers.RotatingFileHandler(
        filename=log_config.FILE_LOG_PATH,
        # mode="w"
    )
    file_handler.setLevel(level=log_config.FILE_LOG_LEVEL)
    file_handler.setFormatter(fmt=formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
