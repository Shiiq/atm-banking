import os
from dataclasses import dataclass, field


@dataclass
class DBConfig:
    """Database config"""

    def __post_init__(self):
        self.DB_PORT = int(self.DB_PORT)

    # POSTGRES DB
    POSTGRES_DB_NAME: str = field(default="atm_dev_default")
    POSTGRES_USER: str = field(default="atm_dev_default_user")
    POSTGRES_PASSWORD: str = field(default="atm_dev_default_password")
    DB_HOST: str = field(default="db")
    DB_PORT: int = field(default=5432)

    # SQLITE DB
    SQLITE_DATABASE_URL: str = field(default="atm_dev.db")

    ECHO: bool = False

    @property
    def postgres_url(self):
        """Postgres database url"""

        return ("postgresql+asyncpg://"
                f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB_NAME}")

    @property
    def sqlite_url(self):
        """SQLITE database url"""

        return f"sqlite+aiosqlite:///./{self.SQLITE_DATABASE_URL}"


def get_db_config() -> DBConfig:
    """Reads database credentials from environment
    and return DBConfig object"""

    postgres_db_name = os.environ.get("POSTGRES_DB_NAME")
    postgres_user = os.environ.get("POSTGRES_USER")
    postgres_password = os.environ.get("POSTGRES_PASSWORD")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")

    return DBConfig(
        POSTGRES_DB_NAME=postgres_db_name,
        POSTGRES_USER=postgres_user,
        POSTGRES_PASSWORD=postgres_password,
        DB_HOST=db_host,
        DB_PORT=db_port
    )
