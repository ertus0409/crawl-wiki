# The code below is influenced from the examples in 'Web scraping with Python' written by Ryan Mitchell
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random



pages = set()  # currently not implemented but can be used to
               #    reduce the redundancy by keeping the record
               #    of already visited sites.
random.seed(datetime.datetime.now())


# Retrieve a list of all Internal Links found in the page
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # Finds all links that begin with '/'
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks



# Retrieve a list of all External Links found in the page
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # Finds all links that starts with 'http' that do not contain the current URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


# Returns a random Internal Link
def getRandomInternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html)
    internalLinks = getInternalLinks(bs, startingPage)
    if len(internalLinks) == 0:
        print('No internal links found, sorry...')
    else:
        return internalLinks[random.randint(0, len(internalLinks) -1)]


# Returns a random External Links
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, features='html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


# Recursively follows external links from given site
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: %s' % externalLink)
    followExternalOnly(externalLink)



# Recursively follows internal links from given site
def followInternalOnly(startingSite):
    internalLink = getRandomInternalLink(startingSite)
    print('Random internal links is: %s' % internalLink)
    followInternalOnly(internalLink)



# followExternalOnly("https://en.wikipedia.org")
# followInternalOnly("https://en.wikipedia.org")
