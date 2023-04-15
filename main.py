from api.api import api

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI


def start_application():
	app = FastAPI()
	app.include_router(api)
	return app


app = start_application()


