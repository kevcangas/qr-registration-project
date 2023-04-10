#Core
from core.db import db
from core.models.supervisers import Supervisers


#Peewee
from peewee import Model, ForeignKeyField


class Workgroups(Model):
    superviser = ForeignKeyField(column_name='superviser_id', field='id', model=Supervisers)

    class Meta:
        database = db
        table_name = 'workgroups'
