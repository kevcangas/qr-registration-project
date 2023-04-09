#Python
import subprocess

#peewee
import peewee

#Propias
from core.settings import Settings


settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

db = peewee.MySQLDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

subprocess.run(['py','-m','pwiz','-e','mysql','-u','root','qr-project','>','mymodels.py'])