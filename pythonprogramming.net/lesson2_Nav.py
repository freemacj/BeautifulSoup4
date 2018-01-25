# lesson from https://pythonprogramming.net/navigating-pages-scraping-parsing-beautiful-soup-tutorial/?completed=/introduction-scraping-parsing-beautiful-soup-tutorial/

# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
source = 'https://pythonprogramming.net/parsememcparseface/'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(source)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'lxml')


# Now, rather than working with the entire soup, we can specify a new Beautiful Soup object. An example might be:
nav = soup.nav
print(nav)

# lets print just the href links found just within the navigation bar
nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))

# find all text found within a div, where the class assigned = 'body'
for div in soup.find_all('div', class_='body'):
    print(div.text)