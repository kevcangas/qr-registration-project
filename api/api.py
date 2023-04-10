#Schemas
from core.schemas.superviser_schema import Supervisers
from core.schemas.workgroup_schema import Workgroups
from core.schemas.users_schema import Users
from core.schemas.sessions_schema import Sessions


#Services
from api.services import get
from api.services import post


#FastAPI
from fastapi import FastAPI
from fastapi import Path, Body


app = FastAPI()


#GET petitions
@app.get(path='/{object}')
def allObjects(
    object: str = Path(
            ...,
            title = "Model",
            description = "Gives all objects of a model",
            example = "supervisers"
        )
    ):
    return get.allObjects(object)


@app.get(path='/{object}/{id_object}')
def idObjects(
    object: str = Path(
            ...,
            title = "Model",
            description = "Object desired",
            example = "supervisers"
        ),
    id_object: int = Path(
            ...,
            title = "Id Object",
            description = "This is the id object desired",
            example = 1
         )
    ):
    return get.idObject(object, id_object)



#POST petitions
@app.post(path='/supervisers/new')
def newSuperviser(objectType: Supervisers = Body(...)):
    return post.createObject('supervisers', objectType)


@app.post(path='/workgroups/new')
def newWorkgroup(objectType: Workgroups = Body(...)):
    return post.createObject('workgroups', objectType)


@app.post(path='/users/new')
def newUser(objectType: Users = Body(...)):
    return post.createObject('users', objectType)


@app.post(path='/sessions/new')
def newSession(objectType: Sessions = Body(...)):
    return post.createObject('sessions', objectType)