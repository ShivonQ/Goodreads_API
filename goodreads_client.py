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
        # here we make an Element Form of our XML so we can iterate through it to get information
        dict_form = ET.fromstring(response.text)
        # This should let me iterate through and get what I want.
        results = parse_best_books(dict_form)
        return results

    def all_books_by_author(self, auth_id):
        base_url = 'https://www.goodreads.com/series/list/'+auth_id+'.xml?key='+secret_key
        response = requests.post(base_url)
        dict_form = ET.fromstring(response.text)
        results = parse_best_books(dict_form)
        return results



def parse_best_books(dict_form):
    all_books = []
    for best_book in dict_form.iter('best_book'):
        # Load up blank dictionary to store book data
        book = {'id': 0, 'title': '', 'author_info': {'auth_id': 0, 'author': ''}}

        '''Due to the structure of the XML parsed by the Element-tree we have to iterate this way to get our data.
           All other methods I tried failed, and this one yields positive results.'''

        for id in best_book.findall('id'):
            book['id'] = id.text
        for title in best_book.findall('title'):
            book['title'] = title.text
        for author_info in best_book.findall('author'):
            book['author_info']['auth_id'] = author_info.find('id').text
            book['author_info']['author'] = author_info.find('name').text
        #     This part could be reinserted at a later time if image support was a thing
        # for image_url in best_book.findall('image_url'):
        #     book['image'] = image_url.text
        all_books.append(book)
    return all_books