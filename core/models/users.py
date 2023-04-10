#Core
from core.db import db
from core.models.workgroups import Workgroups

#Peewee
from peewee import Model, ForeignKeyField, CharField


class Users(Model):
    group = ForeignKeyField(column_name='group_id', field='id', model=Workgroups, null=True)
    name = CharField()

    class Meta:
        database = db
        table_name = 'users'