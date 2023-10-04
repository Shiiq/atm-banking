import os
from dataclasses import dataclass, field


class DatabaseConfigLoaderError(Exception):

    @property
    def msg(self):
        return "Database config cannot be loaded"

    def __str__(self):
        return self.msg


@dataclass(frozen=True)
class DBConfig:
    """Database config"""

    # POSTGRES DB
    POSTGRES_DB: str = field(default="atm_dev_default")
    POSTGRES_USER: str = field(default="atm_dev_default_user")
    POSTGRES_PASSWORD: str = field(default="atm_dev_default_password")
    DB_HOST: str = field(default="db")
    DB_PORT: int = field(default=5432)

    # SQLITE DB
    SQLITE_DATABASE_URL: str = field(default="atm_dev.db")

    ECHO: bool = False

    # LOCAL_LAUNCH: bool = True

    @property
    def postgres_url(self):
        """Postgres database url"""

        return ("postgresql+asyncpg://"
                f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}")

    @property
    def sqlite_url(self):
        """SQLITE database url"""

        return f"sqlite+aiosqlite:///./{self.SQLITE_DATABASE_URL}"


def get_db_config() -> DBConfig:
    """Reads database credentials from environment
    and return DBConfig object"""

    # is_local = os.environ.get("LOCAL")
    # if is_local:
    #     return DBConfig()

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
        raise DatabaseConfigLoaderError

    return DBConfig(
        POSTGRES_DB=postgres_db,
        POSTGRES_USER=postgres_user,
        POSTGRES_PASSWORD=postgres_password,
        DB_HOST=db_host,
        DB_PORT=int(db_port),
    )
