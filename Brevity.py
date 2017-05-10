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

title = soup.body.center.table.tr.next_sibling.next_sibling.div.text.lstrip()
author = soup.select('strong > a')
author = list(author)[0].text
soup.body.center.table.tr.next_sibling.next_sibling.div.decompose() # removes title
#soup.body.center.table.tr.next_sibling.next_sibling.td.decompose() # removes left margin thingy
#soup.body.center.table.tr.next_sibling.next_sibling.td.unwrap() # remove td around story


print 'This is the title:', title
print 'Author name:', author

#story = soup.body.center.table.tr.next_sibling.next_sibling.td.next_sibling.next_sibling
#list(story.children)[3].strong.decompose() # removes the author attribution at the top of story
#list(story.children)[1].br.decompose() # removes the title at the top of the story
#story = unicode(story)
#print story







