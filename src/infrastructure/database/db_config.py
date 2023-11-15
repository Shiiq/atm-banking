from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class DBConfig:
    """
    Database config.
    Default parameters correspond
    to the local type of launch of the application.
    """

    # POSTGRES DB
    postgres_db: Optional[str] = None
    postgres_user: Optional[str] = None
    postgres_password: Optional[str] = None
    db_host: Optional[str] = None
    db_port: Optional[str] = None

    # SQLITE DB
    sqlite_database_url: str = "atm_local_default.db"

    echo: bool = True
    local: bool = True

    @property
    def postgres_url(self):
        """Postgres database url"""
        return (
            "postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.db_host}:{self.db_port}/{self.postgres_db}"
        )

    @property
    def sqlite_url(self):
        """SQLITE database url"""
        return (
            f"sqlite+aiosqlite:///./{self.sqlite_database_url}"
        )
