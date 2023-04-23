#This file contains the information required to connect to the database

#Pydantic
from pydantic import BaseSettings


class Settings(BaseSettings):

    db_name: str = 'b5vb5cw7aryfnst1gn4j'
    db_user: str = 'u0whtm4mf52540nf'
    db_pass: str = 'S0Pl3K1qFISlwtaEsnlj'
    db_host: str = 'b5vb5cw7aryfnst1gn4j-mysql.services.clever-cloud.com'
    db_port: int = 3306