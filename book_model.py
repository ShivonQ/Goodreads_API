from peewee import *
'''This is where the peewee model for a book will be stored'''

"""Make sure that this object stores the goodreads _id.  We will need it later.
    https://www.goodreads.com/search/index.xml?q=Ender&key=4ylN8OWi1dhG5Yhq3PQstA
    that will show you what types of data the server responds with."""


db = SqliteDatabase('MyLibrary.db')


class Base_Model(Model):
    class Meta:
        database = db


class book_model(Base_Model):
    name = CharField(max_length=60, unique=True)
    ISBN = CharField(max_length=1000, unique=True)
    Author = CharField(max_length=100)
    Price = FloatField(null=False, default=0.0)
    Publication = CharField(max_length=100)

