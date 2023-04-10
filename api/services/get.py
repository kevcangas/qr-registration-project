#Models
from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


#Gives the names of all registered supervisers in the database
def allObjects(object):
    if object == 'supervisers': query = Supervisers().select()
    elif object == 'workgroups': query = Workgroups().select()
    elif object == 'users': query = Users().select()
    elif object == 'sessions': query = Sessions().select()
    
    allObjects = []
    for object in query:
        allObjects.append(object.__data__)
    return allObjects


#Gives the parameters of the id object given
def idObject(object,id_object):
    if object == 'supervisers': query = Supervisers.select().where(Supervisers.id == id_object )
    elif object == 'workgroups': query = Workgroups.select().where(Workgroups.id == id_object )
    elif object == 'users': query = Users.select().where(Users.id == id_object )
    elif object == 'sessions': query = Sessions.select().where(Sessions.id == id_object )

    return query[0].__data__