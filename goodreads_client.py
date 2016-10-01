'''This file will be where the goodreads magic happens, more to come later'''
import requests
import xml.etree.ElementTree as ET
from secret_key import secret_key


class goodreads_client():
    def __init__(self):
        self.secret_key = secret_key

    def search(self, parameter):
        # We construct a URL to send to The Goodreads API.  In this case it will take our key, and a
        # search parameter, either a Author, ISBN, or title. in my example file 'test_client.py'
        # you will see that I send the parameter 'Ender' and get a bucnh of weird HTML tags back.
        base_url = 'https://www.goodreads.com/search/index.xml?q='+parameter+'&key='+secret_key
        # An API call MUST be use .post not .get, because that tells the server we expect something back.
        response = requests.post(base_url)
        # TODO: Parse XML to Dictionary so it can be used.
        dict_form = ET.fromstring(response.text)
        # This should let me iterate through and get what I want.

        all_books = []
        for best_book in dict_form.iter('best_book'):
            # Load up blank dictionary to store book data
            book = {'id': 0, 'title': '', 'author_info': {'auth_id': 0, 'author': ''}, 'image': ''}
            print(best_book.attrib)
            for part in best_book.findall('id'):

                print(part.text)
            '''This was useful for figureing out how the tree works'''
            # for work in result:
            #     for piece in work:
            #         print(piece.text)
            #         for author in piece:
            #             print(author.text)
            #             print('---------------------------------------------------------')
            #         # print(piece[8].text)
#         TODO: Get all this data into objects somehow, 7 elements, at least that I care about



