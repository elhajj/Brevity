import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

# start CDATA hack


def CDATA(text=None):
    element = ET.Element('![CDATA[')
    element.text = text
    return element

ET._original_serialize_xml = ET._serialize_xml


def _serialize_xml(write, elem, encoding, qnames, namespaces):
    if elem.tag == '![CDATA[':
        write("<%s%s]]>%s" % (elem.tag, elem.text, elem.tail))
        return
    return ET._original_serialize_xml(
        write, elem, encoding, qnames, namespaces)

ET._serialize_xml = ET._serialize['xml'] = _serialize_xml
# end CDATA hack




address = 'https://www.creativenonfiction.org/brevity/past%20issues/brev28/calderazzo_accident.html'

uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

soup = BeautifulSoup(data, 'html.parser')

title = soup.find('div', {'class': 'storytitle'}).get_text(strip=True)
issue = soup.find('div', {'class': 'issuenumber'}).get_text(strip=True)
issue = issue[7:]

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


print 'Title:', title
print 'Author:', author
print 'Issue', issue
print 'Lines', len(story)

# create xml

rss = ET.Element("rss")
rss.set('version', '2.0')
rss.set('xmlns:excerpt', 'http://wordpress.org/export/1.2/excerpt/')
rss.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
rss.set('xmlns:wfw', 'http://wellformedweb.org/CommentAPI/')
rss.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
rss.set('xmlns:wp', 'http://wordpress.org/export/1.2/')

channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, 'title').text = 'Brevity: A Journal of Concise Literary Nonfiction'
ET.SubElement(channel, 'link').text = 'http://brevitymag.com'
ET.SubElement(channel, 'description').text = 'Brevity: The journal devoted exclusively to the concise literary nonfiction.'
ET.SubElement(channel, 'pubDate').text = 'Fri, 28 Apr 2017 21:01:20 +0000' # is this used in item?
ET.SubElement(channel, 'language').text = 'en-US'
ET.SubElement(channel, 'wp:wxr_version').text = '1.2'
ET.SubElement(channel, 'wp:base_site_url').text = 'http://brevitymag.com'
ET.SubElement(channel, 'wp:base_blog_url').text = 'http://brevitymag.com'
author = ET.SubElement(channel, 'wp:author')
ET.SubElement(author, 'wp:author_id').text = '3'
ET.SubElement(author, 'wp:author_login').text = 'elhajj'
ET.SubElement(author, 'wp:author_email').text = 'tim.elhajj@gmail.com'
ET.SubElement(author, 'wp:author_display_name').text = 'Tim ELhajj'
ET.SubElement(author, 'wp:author_first_name').text = 'Tim'
ET.SubElement(author, 'wp:author_last_name').text = 'Elhajj'
category = ET.SubElement(channel, 'wp:category')
ET.SubElement(category, 'wp:term_id').text = '207'
ET.SubElement(category, 'wp:category-nicename').text = 'issue-28-2008'
ET.SubElement(category, 'wp:category-parent').text = None
ET.SubElement(category, 'wp:cat_name').text = 'Issue 28 / Fall 2008'

item = ET.SubElement(channel, "item")
ET.SubElement(item, 'title').text = None
ET.SubElement(item, 'link').text = None
ET.SubElement(item, 'pubDate').text = None # date?
ET.SubElement(item, 'dc:creator').text = None
ET.SubElement(item, 'guid', isPermaLink='false' ).text = None
ET.SubElement(item, 'description').text = None
ET.SubElement(item, 'content:encoded')
ET.SubElement(item, 'excerpt:encoded').text = None
ET.SubElement(item, 'wp:post_id').text = None
ET.SubElement(item, 'wp:post_date').text = '2000-01-01 19:20:00'
ET.SubElement(item, 'wp:post_date_gmt').text = None
ET.SubElement(item, 'wp:comment_status').text = 'open'
ET.SubElement(item, 'wp:ping_status').text = 'open'
ET.SubElement(item, 'wp:post_name').text = None
ET.SubElement(item, 'wp:status').text = 'draft'
ET.SubElement(item, 'wp:post_parent').text = '0'
ET.SubElement(item, 'wp:menu_order').text = '0'
ET.SubElement(item, 'wp:post_type').text = 'post'
ET.SubElement(item, 'wp:post_password').text = None
ET.SubElement(item, 'wp:is_sticky').text = '0'
ET.SubElement(item, 'category', nicename='characterization', domain='post_tag' ).text = 'characterization'

postmeta = ET.SubElement(item, 'wp:postmeta')
ET.SubElement(postmeta, 'wp:meta_key').text = '_edit_last'
ET.SubElement(postmeta, 'wp:meta_value').text = '2'
postmeta = ET.SubElement(item, 'wp:postmeta')
ET.SubElement(postmeta, 'wp:meta_key').text = 'Author'
ET.SubElement(postmeta, 'wp:meta_value').text = 'JIM BEAM'


tree = ET.ElementTree(rss)
root = tree.getroot()

story = CDATA(story)

root[0][10][6].append(story) # story
root[0][10][0].text = title # title
#root[0][10][3].text = creator

tree.write("filename.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml"
           )