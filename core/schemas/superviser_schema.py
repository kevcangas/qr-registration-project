#pydantic
from pydantic import BaseModel,Field


class Supervisers(BaseModel):
    id: int = Field(
        ...,
        example = 1
    )
    name: str = Field(
        ...,
        example = 'Ricardo'
    )