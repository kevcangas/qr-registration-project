#fastapi
from fastapi import APIRouter
from fastapi.responses import FileResponse


webpage = APIRouter()

@webpage.get(path='/home')
def home():
    return FileResponse(r".\static\home\index.html")


@webpage.get(path='/users')
def users():
    return FileResponse(r".\static\users\index.html")


@webpage.get(path='/users/search')
def users():
    return FileResponse(r".\static\users\search\index.html")