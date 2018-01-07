import urllib
from bs4 import BeautifulSoup
import re

"""creates a unicode list of relative href for 28 past issues"""

address = 'https://www.creativenonfiction.org/brevity/pastissues.htm'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

issue_index = []

issue_index = soup.find_all('a', href=re.compile('past'))
issue_index = filter(lambda tag: tag.attrs.get('target') != '_blank', issue_index)

"""to select href from a result set, use LIST['href'] | LIST[i]['href'] | (in a loop) index['href]  
for tag in issue_index:
    print(tag['href'])"""

print ""
print len(issue_index), 'issues'

full_url = []
baseurl = "https://www.creativenonfiction.org/brevity/"
t = ""

for url in issue_index:
    t = baseurl + url['href']
    full_url.append(t)

""" full_url is not a result set, just a list
for url in full_url:
    print url"""

print ""
print len(full_url), "issues with full urls"

"""use the base links to get all the stories for each issue"""

address = full_url[2]
#address = str(address) # convert from unicode
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'


soup = BeautifulSoup(data, 'html.parser')


issue_number = '0'

address = str(address)


if address[len(address) - 1] == "l":
    issue_number = address[len(address) - 7:-5]
    print issue_number, "This is the issue number from the top of the elif"
elif address[len(address) - 5] == "e":
    print "Create conditions for issues 9,7,4,3,2,and 1"
elif address[len(address) - 5] == "r":
    print "Create conditions for issues 9,7,4,3,2,and 1"
elif address[len(address) - 5] == "v":
    print "Create conditions for issues 9,7,4,3,2,and 1"
elif address[len(address) - 5] == "o":
    print "Create conditions for issues 9,7,4,3,2,and 1"
elif address[len(address) - 5] == "x":
    print "Create conditions for issues 9,7,4,3,2,and 1"
else:
    issue_number = address[len(address) - 6:-4]
    print issue_number, "This is the issue number from bottom of the elif"


issue = []

for link in soup.find_all(href=re.compile(issue_number)):
    print link['href']
    issue.append(link['href'])

print ""
print len(issue), 'pieces in this issue'
print ""