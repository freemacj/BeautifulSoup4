# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://money.cnn.com/data/markets/dow/?xid=cnn_hp_marketbox'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'wsod_fLeft'}) #note the unique data-reactid

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name


# Take out the <div> of name and get its value
price_box = soup.find('span', attrs={'streamfeed': 'MorningstarQuote'}) #note the unique data-reactid

price = price_box.text.strip() # strip() is used to remove starting and trailing
print price


# Take out the <div> of name and get its value
time_box = soup.find('div', attrs={'class': 'wsod_quoteLabelAsOf'}) #note the unique data-reactid

time = time_box.text.strip() # strip() is used to remove starting and trailing
print time
