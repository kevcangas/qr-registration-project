#pydantic
from pydantic import BaseModel, Field


class Users(BaseModel):
    id: int = Field(
        ...,
        example = 1
    )
    group: int = Field(
        ...,
        example = 1
    )
    name: str = Field(
        ...,
        example = 'Kevin'
    )