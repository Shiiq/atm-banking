from dataclasses import dataclass, field


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
