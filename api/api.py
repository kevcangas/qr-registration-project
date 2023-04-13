#Schemas
from core.schemas.superviser_schema import Supervisers, modSupervisers
from core.schemas.workgroup_schema import Workgroups, modWorkgroups
from core.schemas.users_schema import Users, modUsers
from core.schemas.sessions_schema import Sessions, modSessions


#Services
from api.services import get
from api.services import post
from api.services import put


#FastAPI
from fastapi import FastAPI
from fastapi import Path, Body


app = FastAPI()


#GET petitions
@app.get(path='/supervisers', tags=["Supervisers"])
def get_all_supervisers():
    return get.allObjects('supervisers')


@app.get(path='/workgroups', tags=["Workgroups"])
def get_all_workgroups():
    return get.allObjects('workgroups')


@app.get(path='/users', tags=["Users"])
def get_all_users():
    return get.allObjects('users')


@app.get(path='/sessions', tags=["Sessions"])
def get_all_sessions():
    return get.allObjects('sessions')


@app.get(path='/supervisers/{id_object}', tags=["Supervisers"])
def get_id_superviser(
    id_object: int = Path(
            ...,
            title = "Id Object",
            description = "This is the id object desired",
            example = 1
         )
    ):
    return get.idObject('supervisers', id_object)


@app.get(path='/workgroups/{id_object}', tags=["Workgroups"])
def get_id_workgroup(
    id_object: int = Path(
            ...,
            title = "Id Object",
            description = "This is the id object desired",
            example = 1
         )
    ):
    return get.idObject('workgroups', id_object)


@app.get(path='/users/{id_object}', tags=["Users"])
def get_id_user(
    id_object: int = Path(
            ...,
            title = "Id Object",
            description = "This is the id object desired",
            example = 1
         )
    ):
    return get.idObject('users', id_object)


@app.get(path='/sessions/{id_object}', tags=["Sessions"])
def get_id_session(
    id_object: int = Path(
            ...,
            title = "Id Object",
            description = "This is the id object desired",
            example = 1
         )
    ):
    return get.idObject('sessions', id_object)


@app.get(path='/workgroups/{id_workgroup}/users', tags=["Workgroups"])
def get_users_in_workgroup(id_workgroup: int = Path(..., example=1)):
    return get.peopleWorkgroup(id_workgroup)


#POST petitions
@app.post(path='/supervisers/new', tags=["Supervisers"])
def new_superviser(objectType: Supervisers = Body(...)):
    return post.createObject('supervisers', objectType)


@app.post(path='/workgroups/new', tags=["Workgroups"])
def new_workgroup(objectType: Workgroups = Body(...)):
    return post.createObject('workgroups', objectType)


@app.post(path='/users/new', tags=["Users"])
def new_user(objectType: Users = Body(...)):
    return post.createObject('users', objectType)


@app.post(path='/sessions/new', tags=["Sessions"])
def new_session(objectType: Sessions = Body(...)):
    return post.createObject('sessions', objectType)



#PUT petitions
@app.put(path='/supervisers/{id_object}', tags=["Supervisers"])
def mod_superviser(
        id_object: int = Path(..., example=1), 
        objectType: Supervisers = Body(...)
        ):
    return put.modifyObject('supervisers', id_object, objectType)


@app.put(path='/workgroups/{id_object}', tags=["Workgroups"])
def mod_workgroup(
        id_object: int = Path(..., example=1), 
        objectType: Workgroups = Body(...)):
    return put.modifyObject('workgroups', id_object, objectType)


@app.put(path='/users/{id_object}', tags=["Users"])
def mod_user(
        id_object: int = Path(..., example=1)
        , objectType: Users = Body(...)
        ):
    return put.modifyObject('users', id_object, objectType)


@app.put(path='/sessions/{id_object}', tags=["Sessions"])
def mod_session(
        id_object: int = Path(..., example=1), 
        objectType: Sessions = Body(...)
        ):
    return put.modifyObject('sessions', id_object, objectType)