'''This is where the database routes will go.  Since it will be using peewee it should be very few routes.'''
from peewee import *
from peewee_models import *

# db = SqliteDatabase('PersonalLibrary.db')
# db.connect()
# db.create_tables([book_model, author_model], safe=True)


def insert_author_to_table(author_data):
    author_new = author_model(name=author_data['name'], ID=author_data['ID'],  link=author_data['link'])
    author_new.save()
    print(author_new)