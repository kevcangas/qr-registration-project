#Models
from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


#Schemas
import core.schemas as schemas


#Creates a new object with the introduced values
def createObject(object, body_type):
    if object == 'supervisers': newObject = Supervisers(
            id=body_type.id ,
            name=body_type.name
            )
    elif object == 'workgroups': newObject = Workgroups(
            id=body_type.id ,
            superviser=body_type.superviser_id
            )
    elif object == 'users': newObject = Users(
            id=body_type.id, 
            group=body_type.group, 
            name=body_type.name
            )
    elif object == 'sessions': newObject = Sessions(
            id=body_type.id,
            #end_time=body_type.end_time,
            start_time=body_type.start_time,
            user=body_type.user)

    newObject.save(force_insert=True)
    return newObject
