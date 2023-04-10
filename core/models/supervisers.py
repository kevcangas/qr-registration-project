#core
from core.db import db

#peewee
from peewee import Model, CharField, PrimaryKeyField


class Supervisers(Model):
    name = CharField()

    class Meta:
        database = db
        table_name = 'supervisers'