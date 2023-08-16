from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    """Database config"""

    # POSTGRES DB
    POSTGRES_DB: str = "atm_dev"
    POSTGRES_USER: str = "atm_dev_user"
    POSTGRES_PASSWORD: str = "atm_dev_password"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    # SQLITE DB
    SQLITE_DATABASE_URL: str = "atm_dev.db"

    ECHO: bool = False

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


def get_db_config():
    return DBConfig()
