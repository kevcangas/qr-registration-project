#python
from datetime import datetime


#pydantic
from pydantic import BaseModel, Field


class Sessions(BaseModel):
    
    # end_time:datetime = Field(
    #     ...
    # )
    start_time:datetime = Field(
        ...,
        #example=datetime.now
    )
    user:int = Field(
        ...,
        example=1,
        title="user_id"
    )


class modSessions(Sessions):

    id: int = Field(
        ...,
        example = 1
    )
