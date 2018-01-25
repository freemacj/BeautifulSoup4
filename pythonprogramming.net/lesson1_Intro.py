# lesson from https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/

# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
source = 'https://pythonprogramming.net/parsememcparseface/'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(source)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'lxml')

print(soup.title) # Notice how this spits out the title, between the html <title></title> tags?


title = soup.title.text.strip() # strips this down to just the text
print(title)

# Or an even simpler way of doing this can be found here
print(soup.title.string)

# Or a third way
print(soup.title.text)

#find and print all html between <p></p> tags
#print (soup.find_all('p'))

#print just the text found between <p></p> tags NOTE: this will elimate tags found within <p> tags
#for paragraph in soup.find_all('p') :
#    print(paragraph.text)

# get all of the text found on the page
#print(soup.get_text())

#find all of the links within the page
for url in soup.find_all('a'):
    #print(url)
    print(url.get('href'))