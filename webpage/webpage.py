#fastapi
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, FileResponse


webpage = APIRouter()

@webpage.get(path='/home')
def home():
    return FileResponse(".\static\home\index.html")