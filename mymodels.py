from peewee import *

database = MySQLDatabase('qr-project', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Supervisers(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'supervisers'

class Workgroups(BaseModel):
    superviser = ForeignKeyField(column_name='superviser_id', field='id', model=Supervisers)

    class Meta:
        table_name = 'workgroups'

class Users(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=Workgroups, null=True)
    name = CharField()

    class Meta:
        table_name = 'users'

class Sessions(BaseModel):
    end_time = DateTimeField(null=True)
    start_time = DateTimeField()
    user = ForeignKeyField(column_name='user_id', field='id', model=Users)

    class Meta:
        table_name = 'sessions'

