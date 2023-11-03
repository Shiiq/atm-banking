import argparse
import asyncio
import logging
import os

from src.infrastructure.config.config_loader import load_config
from src.infrastructure.logger import setup_root_logger
from src.presentation.api_runner import api_start
from src.presentation.cli_runner import cli_start


async def parse_args():

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

    config = load_config()
    setup_root_logger(log_config=config.logging)

    if args.api:
        logging.warning("preparing the api application")
        await api_start(config=config)
    elif args.cli:
        logging.warning("preparing the cli application")
        await cli_start(config=config)


if __name__ == "__main__":
    asyncio.run(parse_args())
