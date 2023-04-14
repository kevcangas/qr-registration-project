#Models
from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


#fastapi
from fastapi import HTTPException, status


#Function to get the last id of a model
id = lambda model: len(model)+1 if len(model) else 1


#Creates a new object with the introduced values
def createObject(object, body_type):
    try:
        if object == 'supervisers': newObject = Supervisers(
                id=id(Supervisers),
                name=body_type.name
                )
        
        elif object == 'workgroups': newObject = Workgroups(
                id=id(Workgroups) ,
                superviser=body_type.superviser_id
                )
        
        elif object == 'users': newObject = Users(
                id=id(Users), 
                group=body_type.group, 
                name=body_type.name
                )
                
        elif object == 'sessions': newObject = Sessions(
                id=id(Sessions),
                #end_time=body_type.end_time,
                start_time=body_type.start_time,
                user=body_type.user)

    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    ida = newObject.id
    newObject.save(force_insert=True)
    newObject.id = ida

    return {
        "detail": newObject.__data__
    }
