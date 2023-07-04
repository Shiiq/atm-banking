from dataclasses import dataclass

from pydantic import BaseSettings
from pydantic.tools import lru_cache


@dataclass
class DBConfig:
    SQLITE_DATABASE_URL: str = f"sqlite+aiosqlite:///./atm_dev.db"


class _DBConfig(BaseSettings):
    """DATABASE config"""

    # POSTGRES DB
    POSTGRES_DB: str = "atm_dev"
    POSTGRES_USER: str = "atm_dev_user"
    POSTGRES_PASSWORD: str = "atm_dev_password"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    # SQLITE DB
    SQLITE_DATABASE_URL: str = "atm_dev.db"

    @property
    def pg_url(self):
        """Postgres database url"""
        return ("postgresql+asyncpg://"
                f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}")

    @property
    def sqlite_url(self):
        """SQLITE database url"""
        return f"sqlite+aiosqlite:///./{self.SQLITE_DATABASE_URL}"


# @lru_cache()
# def get_db_config():
#     return _DBConfig()
#
#
# db_config = get_db_config()
