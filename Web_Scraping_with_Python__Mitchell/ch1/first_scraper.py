from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        bs_obj = BeautifulSoup(html.read())
        title = bs_obj.body.h1
    except AttributeError:
        return None

    return title


def main():
    url = 'http://www.pythonscraping.com/pages/page1.html'
    title = get_title(url)

    if title is None:
        print('Title could not be found')
    else:
        print(f'Here is the title: {title}')
