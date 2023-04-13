#Pydantic
from pydantic import BaseModel, Field


class Workgroups(BaseModel):

    superviser_id: int = Field(
        ...,
        gt=0,
        example='1',
        title="Superviser's id"
    )


class modWorkgroups(Workgroups):

    id: int = Field(
        ...,
        gt=0,
        example='1'
    )
    
