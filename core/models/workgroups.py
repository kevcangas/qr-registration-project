#Core
from core.db import db


#Peewee
from peewee import Model, IntegerField


class Group(Model):
    superviser_id: int = IntegerField(
        unique=True,
        index=True
    )

    class Meta:
        database = db
