#Core
from core.db import db
from core.models.users import Users

#Peewee
from peewee import Model, ForeignKeyField, DateTimeField


class Sessions(Model):
    end_time = DateTimeField(null=True)
    start_time = DateTimeField()
    user = ForeignKeyField(column_name='user_id', field='id', model=Users)

    class Meta:
        database = db
        table_name = 'sessions'