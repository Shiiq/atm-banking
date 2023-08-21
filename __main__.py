import argparse
import asyncio

from app.presentation.api_runner import api_start
from app.presentation.cli_runner import cli_start


async def parse_args():
    main_parser = argparse.ArgumentParser(description="api or cli")

    group = main_parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-api", help="running the app via api", action="store_true")
    group.add_argument("-cli", help="running the app via cli", action="store_true")

    args = main_parser.parse_args()

    if args.api:
        await api_start()
    elif args.cli:
        await cli_start()
    else:
        print("gggg")


asyncio.run(parse_args())
