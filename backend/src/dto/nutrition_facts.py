from pydantic import BaseModel


class NutritionFacts(BaseModel):
    ingredient_energy: str | None = None  # "32.00kcal"
    ingredient_protein: str | None = None  # "0.00g"
    ingredient_fat: str | None = None  # "0.00g"
    ingredient_carbohydrates: str | None = None  # "7.00g"
