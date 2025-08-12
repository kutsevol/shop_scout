from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cors_origins: List[str]

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
