from pydantic import BaseModel


class Img(BaseModel):
    s150x150: (
        str  # "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s150x150.jpg"
    ) | None = None
    s200x200: (
        str  # "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s200x200.jpg"
    ) | None = None
    s350x350: (
        str  # "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s350x350.jpg"
    ) | None = None
    s1350x1350: (
        str  # "https://img2.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s1350x1350.jpg"
    ) | None = None
