from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


#fastapi
from fastapi import HTTPException, status


def deleteObject(object, id_object):
    try:
        if object == 'supervisers': 
            delObject = Supervisers.get_by_id(id_object)
        
        elif object == 'workgroups':
            delObject = Workgroups.get_by_id(id_object) 
                
        elif object == 'users': 
            delObject = Users.get_by_id(id_object)
            
        elif object == 'sessions': 
            delObject = Sessions.get_by_id(id_object)
                
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    ida = delObject.id
    delObject.delete_instance()
    delObject.id = ida

    return {
        "detail": delObject.__data__
    }