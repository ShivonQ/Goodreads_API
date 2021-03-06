'''This is where the database routes will go.  Since it will be using peewee it should be very few routes.'''
from peewee import *
from peewee_models import *
from tabulate import tabulate

# db = SqliteDatabase('PersonalLibrary.db')
# db.connect()
# db.create_tables([book_model, author_model], safe=True)


def insert_author_to_table(author_data):
    try:
        author_new = author_model.create(name=author_data['name'], id=author_data['ID'],  link=author_data['link'])

        author_new.save()

    except IntegrityError:
        print("author is in database")


def insert_books_to_table(books):
    new_Books = book_model.create(id=books['id'], Title=books['title'], Author_ID=books['auth_id'], Author_Name=books['author_name'])
    new_Books.save()

# def show_all_monsters():
#     big_list = []
#     for monster in Monster_Model:
#         small = compile_monster_record(monster)
#         big_list.append(small)
#     #     TODO: Add a if table is empty dont print anything/skip it all
#     print(tabulate(big_list, headers=['Name', 'Level', 'Max HP', 'Strength', 'Armor', 'XP Value', 'Money'],
#                    tablefmt='pipe'))
#     if len(big_list)<1:
#         return False
#     else:
#         return True


# def compile_monster_record(record):
#     small_list = [record.name, record.level, record.max_hp, record.strength, record.armor, record.xp_value, record.money]
#     return small_list

def displaySavedAuthor():
    big_author = []
    for author in author_model:
        small = compile_authors(author)
        big_author.append(small)
    print(tabulate(big_author, tablefmt='fancy_grid', headers=["Author Name", "ID", "Page Link"]))

def displaySavedBooks():
    big_books = []
    for book in book_model:
        small = compile_record(book)
        big_books.append(small)
    #      print(tabulate(Books, tablefmt="fancy_grid", headers=['Author', 'Author ID', 'Title', 'Book ID']))
    print(tabulate(big_books, tablefmt="fancy_grid", headers=["Author", "Author ID", "Title", "Book ID"]))


def compile_record(record):
    small_list = [record.Author_Name, record.Author_ID, record.Title, record.id]
    return small_list


def compile_authors(author):
    small_list = [author.name, author.id, author.link]
    return small_list