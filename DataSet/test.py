from bs4 import BeautifulSoup

import requests
from requests import HTTPError

r = requests.get("https://www.gutenberg.org/wiki/Fantasy_(Bookshelf)")

data = r.text

soup = BeautifulSoup(data, "lxml")

for link in soup.find_all('li'):
    if link.a:
        title = link.a.get('title')
        if title and 'ebook' in title:
            id = title[6:]
            print(id)

            book_link = 'https://www.gutenberg.org/files/' + id + '/' + id + '.txt'
            try:  # need to open with try
                book = requests.get(book_link)
            except HTTPError as e:
                book_link = 'https://www.gutenberg.org/cache/epub/' + id + '/pg' + id + '.txt'
                try:
                    book = requests.get(book_link)
                except HTTPError as e:
                    book_link = 'https://www.gutenberg.org/files/' + id + '/pg' + id + '-0.txt'
                    try:
                        book = requests.get(book_link)
                    except HTTPError as e:
                        print('other error')
                        continue

            with open(id+'.txt', 'w') as f:
                try:
                    f.write(book.text)
                except UnicodeEncodeError as uniErr:
                    continue

