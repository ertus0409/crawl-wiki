from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="html.parser")


# Using .siblings and .children to navigate in the html tree
# for child in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#     print(child)


# Using regulare expressions (RegEX) to find target elements
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    # print(image)
    print(image["src"])
    print("\n")
