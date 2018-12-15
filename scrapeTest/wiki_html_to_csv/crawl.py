from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError
import re
import csv


# Finding html tables in the html
def scrape_html_table(url):
    # GETting html of the page
    html = urlopen(url)
    # BeautifulSoup object
    bsObj = BeautifulSoup(html, features='html.parser')
    # Parsing the first html table in page
    html_table = bsObj.find('table', {'class': 'wikitable'})
    return html_table



# Parsing html to structure data in csv format
def table_to_file(bsobj, filename):
    with open(filename, 'w', newline="") as csvfile:
        # Creating the HEADER filednames for csv file
        fieldnames = []
        for th in bsobj.find_all('th'):
            fieldnames.append(th.get_text())
        #creating and writing the header of csv file
        writer = csv.writer(csvfile, delimiter=',')
        fieldnames[-1] = fieldnames[-1][:-1]
        print(fieldnames)
        writer.writerow(fieldnames)
        # Extracting DATA VALUES from html_table in bsobj
        data = []
        for tr in bsobj.find('tbody').find_all('tr'):
            dataline = []
            for td in tr.find_all('td'):
                dataline.append(td.get_text()[0:-1])
            data.append(dataline)
        writer.writerows(data)
