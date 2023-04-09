#core
from core import db

#pydantic
from pydantic import BaseModel,Field


class Supervisers(BaseModel):
    name: str = Field(
        ...,
        example = 'Ricardo'
    )