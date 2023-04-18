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
    
    group: int = Field(
        ...,
        example = 1
    )
    