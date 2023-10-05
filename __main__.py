import argparse
import asyncio
import logging

from src.infrastructure.config.alter_log_config import get_log_config
from src.infrastructure.logger.builder import setup_root_logger
from src.presentation.api_runner import api_start
from src.presentation.cli_runner import cli_start


async def parse_args():

    log_config = get_log_config()
    setup_root_logger(log_config=log_config)
    main_parser = argparse.ArgumentParser(description="api or cli")
    group = main_parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-api",
        action="store_true",
        help="running the application via api"
    )
    group.add_argument(
        "-cli",
        action="store_true",
        help="running the src via cli"
    )
    args = main_parser.parse_args()
    if args.api:
        logging.warning("preparing the api application")
        await api_start()
    elif args.cli:
        logging.warning("preparing the cli application")
        await cli_start()


if __name__ == "__main__":
    asyncio.run(parse_args())
