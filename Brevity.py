import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/calderazzo_accident.html'
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

title = soup.find_all('div', 'storytitle')
title = title[0].text.lstrip()

author = soup.select('strong > a')
author = list(author)[0].text

cells = soup.find_all('td')
story = cells[len(cells)-1]
story = story.find_all('p')

shrtaddress = address.rstrip(author+'_'+title+'.html')
addy_append = story[0].find('img').get('src')
story[0].find('img')['src'] = shrtaddress+addy_append
story[0].find('strong').decompose()
new_tag = soup.new_tag('p')
new_tag.string = '__'
story.insert(len(story)-3,new_tag)


print 'This is the title:', title
print 'Author name:', author








