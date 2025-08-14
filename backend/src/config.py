from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cors_origins: list[str] = ["http://localhost:5173"]
    zakaz_api_base_url: str = Field(
        ..., env="ZAKAZ_API_BASE_URL", default="https://stores-api.zakaz.ua"
    )
    user_agent: str = Field(..., env="USER_AGENT", default="price-checker/0.1 (+github.com/you)")

    class Config:
        env_file = "../../.env"
        env_file_encoding = "utf-8"
