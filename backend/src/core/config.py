from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    cors_origins: list[str] = Field(default=["http://localhost:5173"])
    zakaz_api_base_url: str = Field(default="https://stores-api.zakaz.ua")

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")
