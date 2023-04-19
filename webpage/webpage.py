#fastapi
from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse


webpage = APIRouter()


@webpage.get(path='/')
def returnHome():
    return RedirectResponse("http://192.168.1.198:8000/home")


@webpage.get(path='/home')
def home():
    return FileResponse(r".\static\home\index.html")


@webpage.get(path='/users')
def users():
    return FileResponse(r".\static\users\index.html")


@webpage.get(path='/mobile')
def users():
    return FileResponse(r".\static\mobile\index.html")