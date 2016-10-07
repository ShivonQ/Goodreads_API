
from goodreads_client import *
from secret_key import secret_key
grc = goodreads_client()

final_result = grc.search('Ender')
for book in final_result:

    print(book)
