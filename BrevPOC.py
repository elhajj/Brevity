import urllib
from bs4 import BeautifulSoup
import re

# get a story

address = 'https://www.creativenonfiction.org/brevity/pastissues.htm'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

#brev28links = soup.find_all('a', string=re.compile('brev28'))
#brev28links = soup.find_all(href=re.compile('brev28'))

issue_index = []

#for link in soup.find_all(href=re.compile('issue')):
#    print link['href']
#    issue.append(link['href'])

issue_index = soup.find_all('a', href=re.compile('past'))


print len(issue_index), 'issues'
