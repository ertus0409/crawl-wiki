from argparse import ArgumentParser
from crawl import *
from simple_crawl import getInternalLinks, getRandomInternalLink
import datetime



parser = ArgumentParser()
parser.add_argument('-u', '--url', type=str, help='Url of the page to scrape')
parser.add_argument('-m', '--mode', type=str, choices=['crawl', 'scrape'], help='Crawler recursively crawls internal links from the given site')
parser.add_argument('-f', '--filename', type=str, help='Output file name')


args = parser.parse_args()
# print(args.title)


# scrape_html_table() returns a bs object of the table
# table_to_file() formats the given bs object to a file
if args.mode == 'scrape':
    html_table = scrape_html_table(args.url)
    table_to_file(html_table, args.filename)
elif args.mode == 'crawl':
    infinite_crawl(args.url)


# Crawl infinitely
def infinite_crawl(startingPage):
    html_table = scrape_html_table(startingPage)
    table_to_file(html_table, str(datetime.datetime.now()))
    newpage = getRandomInternalLink(startingPage)
    infinite_crawl(newpage)





# Description of the program
print("\n This program converts html data tables in Wikipedia to comma deliminated files.")
