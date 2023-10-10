import os
from dataclasses import dataclass, field

from .exceptions import ConfigLoaderError


@dataclass(frozen=True)
class APIConfig:
    """Application api config"""

    debug: bool = False
    host: str = field(default="127.0.0.1")
    port: int = field(default=10000)
    title: str = field(default="ATM")


def get_api_config():
    """Reads application config from environment
    and return APIConfig object"""

    is_local_condition = "1"
    is_local = os.environ.get("LOCAL")
    if is_local == is_local_condition:
        return APIConfig()

    host = os.environ.get("API_APP_HOST")
    port = os.environ.get("API_APP_PORT")
    title = os.environ.get("API_APP_TITLE")

    config = [host, port, title]
    if not all(config):
        raise ConfigLoaderError("App API config cannot be loaded")

    return APIConfig(
        host=host,
        port=int(port),
        title=title
    )
