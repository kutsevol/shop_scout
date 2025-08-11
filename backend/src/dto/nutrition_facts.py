from pydantic import BaseModel


class NutritionFacts(BaseModel):
    ingredient_energy: str  # "32.00kcal"
    ingredient_protein: str  # "0.00g"
    ingredient_fat: str  # "0.00g"
    ingredient_carbohydrates: str  # "7.00g"
