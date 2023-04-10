#Pydantic
from pydantic import BaseModel, Field


class Workgroups(BaseModel):
    id: int = Field(
        ...,
        gt=0,
        example='1'
    )
    superviser_id: int = Field(
        ...,
        gt=0,
        example='1'
    )
