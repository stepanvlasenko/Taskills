from peewee import *
from playhouse.sqlite_ext import JSONField

db = SqliteDatabase('./backend/dev.db')

class BaseModel(Model):
    class Meta:
        database = db

class Sight(BaseModel):
    title = CharField()
    description = CharField()
    images = JSONField()
    address = CharField()
    latitude = FloatField()
    longitude = FloatField()
    keywords = JSONField()