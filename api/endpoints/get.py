#Models



#FastAPI
from fastapi import Path


def getGroups(
        group_id: int = Path(
            ...,
            gt=0,
            title = "Group ID",
            description = "This is the group ID. It's required",
            example = 1
        )
    ):
    pass