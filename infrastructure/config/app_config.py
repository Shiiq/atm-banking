from pydantic import BaseSettings


class AppConfig(BaseSettings):
    """Application config"""

    host: str = "127.0.0.1"
    port: int = 7000

    debug: bool = False
    title: str = "atm"

    default_response_class = ...


def get_db_config():
    return AppConfig()
