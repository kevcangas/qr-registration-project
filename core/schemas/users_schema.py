#python
from typing import Optional


#pydantic
from pydantic import BaseModel, Field


class Users(BaseModel):
    
    # group: int = Field(
    #     ...,
    #     example = 1,
    #     title='group_id'
    # )
    name: str = Field(
        ...,
        example = 'Kevin'
    )


class modUsers(BaseModel):
    
    group: Optional[int] = Field(
        ...,
        example = 1
    )
    