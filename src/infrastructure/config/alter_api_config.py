import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class APIConfig:
    """Application api config"""

    debug: bool = False
    host: str = field(default="127.0.0.1")
    port: int = field(default=7000)
    title: str = field(default="ATM")


def get_api_config():
    return APIConfig()
