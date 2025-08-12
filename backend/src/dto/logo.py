from pydantic import BaseModel


class Logo(BaseModel):
    s32x32: (
        str  # "https://img2.zakaz.ua/upload.version_1.0.c8beac3b09d1e2741bc9052fcf3d6f42.32x32.png"
    ) | None = None
    s16x16: (
        str  # "https://img3.zakaz.ua/upload.version_1.0.c8beac3b09d1e2741bc9052fcf3d6f42.16x16.png"
    ) | None = None
    s64x64: (
        str  # "https://img3.zakaz.ua/upload.version_1.0.c8beac3b09d1e2741bc9052fcf3d6f42.64x64.png"
    ) | None = None
