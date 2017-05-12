import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/calderazzo_accident.html'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/madden_catch.html'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/svoboda_catholic.html'
address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/doyle_child.html'

uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

title = soup.find('div', {'class': 'storytitle'}).get_text(strip=True)
issue = soup.find('div', {'class': 'issuenumber'}).get_text(strip=True)
issue = issue[7:]

#title = soup.find_all('div', 'storytitle')
#title = title[0].text.lstrip()

author = soup.title.get_text(strip=True)
author = author[12:].upper() # this will break < issue 10

story = soup.find_all('p')

shrtaddress = address[:64-len(address)] # this will break < issue 10
image = soup.find_all('img')
if len(soup.find_all('img')) != 2:
    print "image is probably broken for", title
image = image[1]
addy_append = image.get('src')
image['src'] = shrtaddress+addy_append


#story[0].find('strong').decompose()
#new_tag = soup.new_tag('p')
#new_tag.string = '__'
#story.insert(len(story)-3,new_tag)



print 'This is the title:', title
print 'Author name:', author

for p in story:
    print p.text

for p in story:
    print p






