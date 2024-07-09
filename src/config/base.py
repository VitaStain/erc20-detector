from pydantic import Extra
from pydantic_settings import BaseSettings

from src.config.database import DataBaseSettings, DatabaseHelper


class Settings(BaseSettings):
    class Config:
        extra = Extra.allow
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"

    host: str = "0.0.0.0"
    port: int = "8000"
    workers_count: int = 1
    reload: bool = False
    debug: bool = False

    db: DataBaseSettings


settings = Settings()


db_helper = DatabaseHelper(settings.db.get_url(), settings.db.echo)