#This file contains the information required to connect to the database

#Pydantic
from pydantic import BaseSettings


class Settings(BaseSettings):

    db_name: str = 'qr-project'
    db_user: str = 'root'
    db_pass: str = ''
    db_host: str = '127.0.0.1'
    db_port: int = 3306