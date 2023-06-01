# from pathlib import Path
#
# from pydantic import BaseSettings
# from pydantic.tools import lru_cache
#
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
#
#
# class Settings(BaseSettings):
#     """Project settings"""
#
#     # POSTGRES DB
#     POSTGRES_DB: str
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     DB_HOST: str
#     DB_PORT: str
#
#     # SQLITE DB
#     SQLITE_DATABASE_URL: str
#
#     @property
#     def pg_database_url(self):
#         """Postgres database url"""
#         return ("postgresql+asyncpg://"
#                 f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
#                 f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}")
#
#     class Config:
#         env_file = ".env.dev"
#
#
# @lru_cache()
# def get_settings():
#     return Settings()
#
#
# settings = get_settings()
