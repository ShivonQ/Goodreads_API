'''This file will be where the goodreads magic happens, more to come later'''
import requests
from secret_key import secret_key


class goodreads_client():
    def __init__(self):
        self.secret_key = secret_key

    def search(self, parameter):
        base_url = 'https://www.goodreads.com/search/index.xml?q='+parameter+'&key='+secret_key
        response = requests.get(base_url)
        print(response.url)

