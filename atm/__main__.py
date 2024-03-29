import argparse
import asyncio
import logging

from atm.infrastructure.config import load_config
from atm.infrastructure.logger import setup_root_logger
from atm.presentation.api_runner import api_start
from atm.presentation.cli_runner import cli_start


def parse_args():

    main_parser = argparse.ArgumentParser(description="api or cli")
    group = main_parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-api",
        action="store_true",
        help="run the application via api"
    )
    group.add_argument(
        "-cli",
        action="store_true",
        help="run the application via cli"
    )
    args = main_parser.parse_args()
    return args


async def main():
    """Entry point for the running app locally."""

    args = parse_args()
    config = load_config()
    setup_root_logger(log_config=config.logging)

    if args.api:
        logging.warning("preparing the application api")
        await api_start(config=config)
    elif args.cli:
        logging.warning("preparing the application cli")
        await cli_start(config=config)


if __name__ == "__main__":
    asyncio.run(main())
