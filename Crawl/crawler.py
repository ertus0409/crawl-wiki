# Crawler class to define and perform the actual
#   crawling processes
import re
import requests
from bs4 import BeautifulSoup
from website import Content, Website
import time



# Crawler class aims to crawl wikipedia to identify the links containing
#   html table for the purpose of presenting large data.
class Crawler:
    # gets a Website object as an argument
    def __init__(self, site):
        self.site = site
        self.visited = []

    # GET request to given url returning bsObj
    def getPage(self, url):
        try:
            req =requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')


    # Getting the necessary information form the bsObj based on the
    #   given css selector.
    # def safeGet(self, pageObj, selector):
    #     selectedElems = pageObj.select(selector)
    #     if (selectedElems is not None) and (len(selectedElems) > 0):
    #         return '\n'.join([elem.get_text() for elem in selectedElems])
    #     return ''



    # Collecting little infromation from the page to have an
    #   overview of how usefull the the url will be.
    def parse(self, url):
        time.sleep(2) # to avoid overloading the webserver w/ many requests
        bs = self.getPage(url)
        if bs is not None:
            title = bs.find('h1', {'id': 'firstHeading'}).get_text()
            html_table = bs.find('table', {'class': 'wikitable'})
            if html_table is not None:
                table = True
            else:
                table = False
            content = Content(url, title, table)
            content.print()



    # The crawling process can begin with the crawl() function,
    #   after the Crawl object is created with the necessary
    #   information.
    def crawl(self):
        bs = self.getPage(self.site.url)
        targetPages = bs.find_all('a', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                targetPage = '{}{}'.format(self.site.base_url, targetPage)
                self.parse(targetPage)





# Simple implemtation of the CRAWL class
wiki = Website('Countries', 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population', '^(/wiki)((?!:).)*$')
crawler = Crawler(wiki)
crawler.crawl()
