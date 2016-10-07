'''This is where the database routes will go.  Since it will be using peewee it should be very few routes.'''
from peewee import *
from book_model import *

db = SqliteDatabase('PersonalLibrary.db')
db.connect()
db.create_table(book_model, author_model)


def insert_author_to_table(author_data):
    author_new = author_model(ID=author_data['ID'], name=author_data['name'],  link=author_data['link'])
    author_new.save()
    print(author_new)