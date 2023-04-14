#python
from datetime import datetime


#pydantic
from pydantic import BaseModel, Field


class Sessions(BaseModel):
    
    start_time:datetime = Field(
        ...,
        #example=datetime.now
    )
    user:int = Field(
        ...,
        example=1,
        title="user_id"
    )


class modSessions(BaseModel):

    end_time:datetime = Field(
        ...
    )

