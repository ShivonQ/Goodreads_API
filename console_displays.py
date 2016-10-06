'''This is where all console display & menu strings will be stored'''


class menu_display:
    @staticmethod
    def main_menu(self):
        menu = ('\t1) Search a book\n'
                '\t2) find a author by name\n'
                '\t3) Quit \n'
                '\nWhat do you want ??? : ')
        return menu

    @staticmethod
    def sub_menu(self):
        sub_menu = (
            '\nSearch a Book\n'
            '\t1) By Author\n'
            '\t2) By ISBN\n'
            '\t3) By Title\n'
            '\t4) Back'
            '\nEnter Selection'
        )
        return sub_menu
