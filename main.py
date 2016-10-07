"""This file will run the programs main loops, show the displays and generally
   bring together the other files into a cohesive unit"""
from tabulate import *
from Validator import *
from goodreads_client import goodreads_client as ap
from database import *
from console_displays import menu_display
from book_model import *


def show_menu():
    """ displays the menu for the user
    checks if user has chosen the right choice from the list
    and calls methods to complete the action"""
    menu = menu_display.main_menu()
    menu_choice = int(input(menu))
    while not is_whole_number(menu_choice, range(1, 5)):
        menu_choice = int(input("Invalid entry, please select from the list !!!"))
    if menu_choice == 1:
        search_book()
    if menu_choice == 2:
        search_for_author()
    elif menu_choice == 3:

       exit(3)


def search_for_author():
    author_name = get_string1_input("find auther by name")
    author_data = ap.author_by_name(author_name)
    print("ID: {}\nName: {}\nLink: {}\n".format(author_data['ID'], author_data['name'], author_data['link']))
    insert_author_to_table(author_data)


def search_book():
    """Sub-menu for searching a book option."""
    menu_string = menu_display.sub_menu()
    while True:
        menu_choice = get_user_int(menu_string)
        if menu_choice == 1:
            try:
                author_name = get_string1_input('Enter author''s name')
                Books = ap.search(author_name)
                print("The books are:")
                print(tabulate(Books, tablefmt="fancy_grid"))
            except:
               print(" No data found !!!")
        elif menu_choice == 2:
            isbn = get_string1_input("Enter ISBN for the book")
            Books = ap.search(isbn)
            print("The books are:")
            print(tabulate(Books, tablefmt="fancy_grid"))
        elif menu_choice ==3:
            title = get_string1_input("Enter the book-title")
            Books = ap.search(title)
            print(tabulate(Books, tablefmt="fancy_grid"))
        elif menu_choice == 4:
            return


def main():
    menu_display.initial_console_display()
    show_menu()
    db.create_table([book_model, author_model])

main()
