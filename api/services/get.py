#Models
from core.models.supervisers import Supervisers
from core.models.workgroups import Workgroups
from core.models.users import Users
from core.models.sessions import Sessions


#fastapi
from fastapi import HTTPException, status


#Gives the names of all registered supervisers in the database
def allObjects(object):
    try:
        if object == 'supervisers': query = Supervisers().select()
        elif object == 'workgroups': query = Workgroups().select()
        elif object == 'users': query = Users().select()
        elif object == 'sessions': query = Sessions().select()
        
        allObjects = []
        for object in query:
            allObjects.append(object.__data__)
        allObjects = [("detail", allObjects)]
        return dict(allObjects)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#Gives the parameters of the id object given
def idObject(object,id_object):
    try:
        if object == 'supervisers': query = Supervisers.select().where(Supervisers.id == id_object )
        elif object == 'workgroups': query = Workgroups.select().where(Workgroups.id == id_object )
        elif object == 'users': query = Users.select().where(Users.id == id_object )
        elif object == 'sessions': query = Sessions.select().where(Sessions.id == id_object )

        return {
            "detail": query[0].__data__
        }
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#Gives the users in a workgroup and the superviser
def peopleWorkgroup(work_group_id):
    try:
        users_in_workgroup = Users.select().where(Users.group == work_group_id)
        workgroup_selected = Workgroups.get_by_id(work_group_id)
        superviser_in_group = Supervisers.get_by_id(workgroup_selected.superviser)

        people = [("superviser", superviser_in_group.name)]
        users = []
        for person in users_in_workgroup:
            users.append(person.__data__)
        people.append(("users", users))
        return {
            "detail": dict(people)
        }
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
