from pydantic import BaseModel


class NutritionFacts(BaseModel):
    ingredient_energy: str | None = None
    ingredient_protein: str | None = None
    ingredient_fat: str | None = None
    ingredient_carbohydrates: str | None = None
