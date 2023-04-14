from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


#fastapi
from fastapi import HTTPException, status


#This function modify the values of a entry model
def modifyObject(object, id_object, body_type):
    try:
        if object == 'supervisers': 
             if Supervisers.get_by_id(id_object):
                modObject = Supervisers(
                                id=id_object,
                                name=body_type.name
                                )
        
        elif object == 'workgroups':
             if Workgroups.get_by_id(id_object): 
                modObject = Workgroups(
                                id=id_object,
                                superviser=body_type.superviser_id
                                )
        
        elif object == 'users': 
             if Users.get_by_id(id_object):
                modObject = Users(
                                id=id_object, 
                                group=body_type.group, 
                                name=body_type.name
                                )
                
        elif object == 'sessions': 
            if Sessions.get_by_id(id_object):
                modObject = Sessions(
                                id=id_object,
                                end_time=body_type.end_time,
                                #start_time=body_type.start_time,
                                #user=body_type.user
                                )
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    ida = modObject.id
    modObject.save()
    modObject.id = ida

    return {
        "detail": modObject.__data__
    }