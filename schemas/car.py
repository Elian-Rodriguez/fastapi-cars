from pydantic import BaseModel, Field


class SportsCar(BaseModel):
    id: int = None
    make: str = Field(min_length=2, max_length=30)
    model: str = Field(min_length=2, max_length=30)
    year: int = Field(ge=1900, le=2022)
    horsepower: int = Field(ge=0)
    top_speed: float = Field(ge=0, le=1200)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "make": "Ferrari",
                "model": "458 Italia",
                "year": 2015,
                "horsepower": 570,
                "top_speed": 202.0
            }
        }
