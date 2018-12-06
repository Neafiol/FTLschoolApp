
import sqlite3
from datetime import date
from peewee import *

db = SqliteDatabase('../db.sqlite3')

class Puple(Model):
    login=TextField(null = True)
    password=TextField(null = True)
    name=TextField(null = True)
    surname = TextField(null = True)
    email = TextField(null = True)
    phone = TextField(null = True)
    class_nom = IntegerField(null = True)
    class_type = IntegerField(null = True)

    class Meta:
        database = db
        db_table='Puple'

class Messages(Model):
    text=TextField(null=True)
    header=TextField(null=True)
    puple_id=TextField(null=True)
    class_nom = IntegerField(null=True)
    class_type = IntegerField(null=True)

    class Meta:
        database = db
        db_table='Messages'


Messages.create_table()
# uncle_bob = Subs(name='Bob', tel_id=121212)
# uncle_bob.save()