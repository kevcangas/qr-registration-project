#Models
from core.models.supervisers import Supervisers


#FastAPI
from fastapi import Path


#Gives the names of all registred supervisers in the database
def getSupervisers():
    query = Supervisers().select()
    supervisers = []
    for superviser in query:
        supervisers.append(superviser.name)
    return supervisers