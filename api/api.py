
from api.services import get


#FastAPI
from fastapi import FastAPI


app = FastAPI()


#GET petitions
@app.get(path='/supervisers')
def Supervisers():
    return get.getSupervisers()