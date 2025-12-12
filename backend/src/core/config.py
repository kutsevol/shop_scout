from pathlib import Path
from typing import Literal

import tomli
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent
PROJECT_FILE = "pyproject.toml"


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=["../.env", ".env"], env_file_encoding="utf-8")

    cors_origins: list[str] = Field(default=["http://localhost:5173"])
    user_agent: str | None = None
    zakaz_api_base_url: str = Field(default="https://stores-api.zakaz.ua")
    log_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = Field(default="INFO")
    root_path: str = Field(default="/shop_scout")
    database_url: str = Field(default="postgresql+asyncpg://user:@localhost:5432/shop_scout")
    database_url_sync: str = Field(default="postgresql+psycopg://user:@localhost:5432/shop_scout")
    db_echo: bool = False


with open(BASE_DIR.joinpath(PROJECT_FILE), "rb") as file:
    pyproject_toml = tomli.load(file)

PROJECT_VERSION = pyproject_toml["project"]["version"]
settings = AppSettings()
