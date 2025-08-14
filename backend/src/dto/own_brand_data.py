from pydantic import BaseModel


class OwnBrandData(BaseModel):
    name: str | None = None
