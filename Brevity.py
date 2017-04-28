import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# get a story

address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/calderazzo_accident.html'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

# print soup.prettify()