from pydantic import BaseModel, Field


class NutritionFacts(BaseModel):
    ingredient_energy: str | None = Field(default=None)
    ingredient_protein: str | None = Field(default=None)
    ingredient_fat: str | None = Field(default=None)
    ingredient_carbohydrates: str | None = Field(default=None)
