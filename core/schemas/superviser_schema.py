#pydantic
from pydantic import BaseModel,Field


class Supervisers(BaseModel):
    
    name: str = Field(
        ...,
        title = "Superviser's name", 
        example = 'Ricardo'
    )


class modSupervisers(Supervisers):
    
    id: int = Field(
        ...,
        example = 1
    )