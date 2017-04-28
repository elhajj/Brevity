import urllib
from bs4 import BeautifulSoup
import re

# get a story

address = 'https://www.creativenonfiction.org/brevity/past%20issues/index28.html'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

#brev28links = soup.find_all('a', string=re.compile('brev28'))
#brev28links = soup.find_all(href=re.compile('brev28'))

issue = []

for link in soup.find_all(href=re.compile('28')):
    print link['href']
    issue.append(link['href'])

print len(issue), 'pages in this issue'