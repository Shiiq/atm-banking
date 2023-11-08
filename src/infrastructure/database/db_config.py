from dataclasses import dataclass


@dataclass(frozen=True)
class DBConfig:
    """
    Database config.
    Default parameters correspond
    to the local type of launch of the application.
    """

    # POSTGRES DB
    postgres_db: str = None
    postgres_user: str = None
    postgres_password: str = None
    db_host: str = None
    db_port: int = None

    # SQLITE DB
    sqlite_database_url: str = "atm_local_default.db"

    echo: bool = False
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
        return f"sqlite+aiosqlite:///./{self.sqlite_database_url}"
