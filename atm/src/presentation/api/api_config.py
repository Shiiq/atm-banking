from dataclasses import dataclass


@dataclass(frozen=True)
class APIConfig:
    """
    Application api config.
    Default parameters correspond
    to the local type of launch of the application.
    """

    debug: bool = True
    title: str = "ATMBanking api"
    host: str = "127.0.0.1"
    port: int = 10000
