"""This file will run the programs main loops, show the displays and generally
   bring together the other files into a cohesive unit"""
from tabulate import *
from Validator import *
from goodreads_client import goodreads_client as ap


def show_menu():
    """ displays the menu for the user
    checks if user has chosen the right choice from the list
    and calls methods to complete the action"""
    menu = ('\t1) Search a book\n'
            '\t2) Quit \n'
            '\nWhat do you want ??? : ')
    menu_choice = int(input(menu))
    while not is_whole_number(menu_choice, range(1, 5)):
        menu_choice = int(input("Invalid entry, please select from the list !!!"))
    if menu_choice == 1:
            search_book()
    elif menu_choice == 2:
       exit(2)


def search_book():
    """Sub-menu for register course option."""

    menu_string = (
        '\nSearch a Book\n'
        '\t1) By Author\n'
        '\t2) By ISBN\n'
        '\t3) Back\n'
        '\nEnter Selection'
    )
    while True:
        menu_choice = get_user_int(menu_string)
        if menu_choice == 1:
           try:
            author_name = get_string1_input('Enter author''s name')
            Books = ap.all_books_by_author(author_name)
            print("The books are:")
            print(tabulate(Books, tablefmt="fancy_grid"))
           except:
               print(" No data found !!!")

        elif menu_choice == 2:
            isbn = get_string1_input("Enter ISBN for the book")
            Books = ap.all_books_by_author(isbn)
            print("The books are:")
            print(tabulate(Books, tablefmt="fancy_grid"))
        elif menu_choice == 3:
            return


def main():
    print('\033[1m' + '\033[94m' + "The Program starts here !!! " + '\033[0m')
    print("***************************")
    print("Menu : ")
    show_menu()

main()