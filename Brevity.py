import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev26hotcold/panning_vietnam.html'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/calderazzo_accident.html'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/madden_catch.html'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/svoboda_catholic.html'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/doyle_child.html'
#known issues
address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev18/borrowman_shillings.htm'
#address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev25/gregory_enormous.htm'

uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

#title = soup.find('div', {'class': 'storytitle'}).get_text(strip=True)
#issue = soup.find('div', {'class': 'issuenumber'}).get_text(strip=True)
#issue = issue[7:]

#author = soup.title.get_text(strip=True)
#author = author[12:].upper() # this will break < issue 10

author = soup.find_all(text=re.compile('^By'))
author = author[0].string
author = author[3:]

story = soup.find_all('p')

shrtaddress = address[:64-len(address)] # this will break < issue 10
image = soup.find_all('img')
if len(soup.find_all('img')) != 2:
    print "image is probably broken for", title
# iterate through all images, addding address to src and find a way to identify the img in story
image = image[1]
addy_append = image.get('src')
image['src'] = shrtaddress+addy_append

'''
#insert the "__", remove the hr
hr = soup.find_all('hr', align='left')
if len(hr) != 1:
    hr = soup.find_all('hr')
hr = hr[0].wrap(soup.new_tag('p'))
hr = hr.p
tag = soup.new_tag('p')
tag.string = '__\n'
hr.insert(0,tag)
'''
'''
ps = soup.find_all('p')

for i in ps:
    print i
    if "Brevity" in i.text:
        i.decompose()        
    if "strong" in i.name:
        i.decompose()
'''


#story[0].find('strong').decompose()




#print 'Title:', title
print 'Author:', author
#print 'Issue', issue

for p in story:
    print p.text

for p in story:
    print p






