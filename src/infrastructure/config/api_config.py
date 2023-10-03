from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """Application config"""

    host: str = "127.0.0.1"
    port: int = 7000

    debug: bool = False
    title: str = "atm"


def get_app_config():
    return AppConfig()
