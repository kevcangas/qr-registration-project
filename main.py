#api
from api.api import api
from webpage.webpage import webpage


#fastapi
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.routing import Mount, APIWebSocketRoute


#Function to start the app
def start_application():
	app = FastAPI()

	#Parts of the app
	app.include_router(api)
	app.include_router(webpage)

	#Directory where the static files can be request
	app.mount("/static", app=StaticFiles(directory="static"), name="static") 
	return app


app = start_application()


