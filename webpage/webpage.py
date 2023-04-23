#fastapi
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


webpage = APIRouter()
templates = Jinja2Templates(directory="static")


@webpage.get(path='/', tags=['Webpage'])
def return_Home():
    return RedirectResponse("/home")


@webpage.get(path='/home', tags=['Webpage'])
def home(request: Request):
    return templates.TemplateResponse("/home/index.html",{"request": request})
    

@webpage.get(path='/users', tags=['Webpage'])
def users(request: Request):
    return templates.TemplateResponse("/users/index.html",{"request": request})


@webpage.get(path='/mobile', tags=['Webpage'])
def users(request: Request):
    return templates.TemplateResponse("/mobile/index.html",{"request": request})


@webpage.get(path='/workgroups', tags=['Webpage'])
def users(request: Request):
    return templates.TemplateResponse("/workgroups/index.html",{"request": request})