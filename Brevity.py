import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

# get links for an issue

address = 'https://www.creativenonfiction.org/brevity/past%20issues/index28.html'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')
issue = []

for link in soup.find_all(href=re.compile('28')):
    #print link['href']
    issue.append(link['href'])

print len(issue), 'pages in this issue'

# get a single story and extract HTML

address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/calderazzo_accident.html'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

print soup.title

