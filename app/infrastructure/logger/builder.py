import logging
from logging import Logger

from app.infrastructure.config.log_config import LogConfig


def build_logger(log_config: LogConfig) -> Logger:

    logger = logging.getLogger(name=log_config.NAME)
    formatter = logging.Formatter(fmt=log_config.LOG_FORMAT,
                                  datefmt=log_config.DATE_FORMAT)
    handler = logging.StreamHandler()
    handler.setLevel(level=log_config.LEVEL)
    handler.setFormatter(fmt=formatter)

    return logger
