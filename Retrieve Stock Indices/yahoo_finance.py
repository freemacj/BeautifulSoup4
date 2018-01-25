# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://finance.yahoo.com/quote/%5EDJI?p=^DJI'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'data-reactid': '7'}) #note the unique data-reactid

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name


# Take out the <div> of name and get its value
name_box2 = soup.find('span', attrs={'data-reactid': '9'}) #note the unique data-reactid

name2 = name_box2.text.strip() # strip() is used to remove starting and trailing

print name2

# Take out the <div> of name and get its value
time_box = soup.find('div', attrs={'id': 'quote-market-notice'}) #note the unique id

time = time_box.text.strip() # strip() is used to remove starting and trailing

print time