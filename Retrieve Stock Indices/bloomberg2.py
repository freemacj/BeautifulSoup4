# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

print(soup.title.text)

# find all text found within a h1 tag, where the class assigned = 'name'
for h1 in soup.find_all('h1', class_='name'):
    print(h1.text.strip())

# find all text found within a div, where the class assigned = 'price'
for div in soup.find_all('div', class_='price'):
    print(div.text)

# find all text found within a div, where the class assigned = 'price-datetime'
for div in soup.find_all('div', class_='price-datetime'):
    print(div.text.strip())