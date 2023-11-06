from dataclasses import dataclass


@dataclass(frozen=True)
class APIConfig:
    """Application api config"""

    debug: bool = True
    title: str = "ATMBanking api"
    host: str = "0.0.0.0"
    port: int = 10000
