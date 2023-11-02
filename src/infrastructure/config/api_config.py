import os
from dataclasses import dataclass, field

from .exceptions import ConfigLoaderError


@dataclass(frozen=True)
class APIConfig:
    """Application api config"""

    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 10000


def get_api_config():
    """Reads application config from environment
    and return APIConfig object"""

    is_local_condition = "1"
    is_local = os.environ.get("LOCAL")
    if is_local == is_local_condition:
        return APIConfig()

    debug = os.environ.get("DEBUG")
    host = os.environ.get("API_APP_HOST")
    port = os.environ.get("API_APP_PORT")

    config = [debug, host, port]
    if not all(config):
        raise ConfigLoaderError("App API config cannot be loaded")

    return APIConfig(
        debug=False,
        host=host,
        port=int(port),
    )
