import argparse
import asyncio
import logging

from src.infrastructure.config.alter_log_config import get_log_config
from src.infrastructure.logger.builder import setup_root_logger
from src.presentation.api_runner import api_start
from src.presentation.cli_runner import cli_start


