from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


def modifyObject(object, body_type):
    if object == 'supervisers': newObject = Supervisers(
            id=id(Supervisers),
            name=body_type.name
            )
    
    elif object == 'workgroups': newObject = Workgroups(
            id=id(Workgroups),
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
            user=body_type.user
            )

    newObject.save(force_insert=True)
    return body_type