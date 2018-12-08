from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# bsObj = BeautifulSoup(html.read(), features="html.parser")
# print(bsObj.h1.get_text())


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title



title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
