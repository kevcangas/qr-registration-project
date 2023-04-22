#fastapi
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


webpage = APIRouter()


templates = Jinja2Templates(directory="static")


@webpage.get(path='/', response_class=HTMLResponse)
def returnHome():
    return RedirectResponse("/home")


@webpage.get(path='/home', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("/home/index.html",{"request": request})
    

@webpage.get(path='/users', response_class=HTMLResponse)
def users(request: Request):
    return templates.TemplateResponse("/users/index.html",{"request": request})


@webpage.get(path='/mobile', response_class=HTMLResponse)
def users(request: Request):
    return templates.TemplateResponse("/mobile/index.html",{"request": request})