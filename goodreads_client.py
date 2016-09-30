'''This file will be where the goodreads magic happens, more to come later'''
import requests
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
        print(response.text)



