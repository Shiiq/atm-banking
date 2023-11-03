import os
from dataclasses import dataclass, field

from .exceptions import ConfigLoaderError


@dataclass(frozen=True)
class DBConfig:
    """Database config"""

    # POSTGRES DB
    postgres_db: str = None
    postgres_user: str = None
    postgres_password: str = None
    db_host: str = None
    db_port: int = None

    # SQLITE DB
    sqlite_database_url: str = field(default="atm_local_default.db")

    echo: bool = field(default=False)
    local: bool = field(default=True)

    @property
    def is_local(self):
        return self.local

    @property
    def postgres_url(self):
        """Postgres database url"""
        return ("postgresql+asyncpg://"
                f"{self.postgres_user}:{self.postgres_password}"
                f"@{self.db_host}:{self.db_port}/{self.postgres_db}")

    @property
    def sqlite_url(self):
        """SQLITE database url"""
        return f"sqlite+aiosqlite:///./{self.sqlite_database_url}"


def get_db_config() -> DBConfig:
    """Reads database credentials from environment
    and return DBConfig object"""

    is_local_condition = "1"
    is_local = os.environ.get("LOCAL")
    if is_local == is_local_condition:
        return DBConfig(local=True)

    postgres_db = os.environ.get("POSTGRES_DB")
    postgres_user = os.environ.get("POSTGRES_USER")
    postgres_password = os.environ.get("POSTGRES_PASSWORD")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")

    db_credentials = [
        postgres_db,
        postgres_user,
        postgres_password,
        db_host,
        db_port
    ]
    if not all(db_credentials):
        raise ConfigLoaderError("Database config cannot be loaded")

    return DBConfig(
        postgres_db=postgres_db,
        postgres_user=postgres_user,
        postgres_password=postgres_password,
        db_host=db_host,
        db_port=int(db_port),
    )
