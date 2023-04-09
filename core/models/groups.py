#Pydantic
from pydantic import BaseModel
from pydantic import Field


class Group(BaseModel):
    superviser_id: int = Field(
        ...,
        gt = 0
    )