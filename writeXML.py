import xml.etree.ElementTree as ET

# wordpress required
rss = ET.Element("rss")
rss.set('version', '2.0')
rss.set('xmlns:excerpt', 'http://wordpress.org/export/1.2/excerpt/')
rss.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
rss.set('xmlns:wfw', 'http://wellformedweb.org/CommentAPI/')
rss.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
rss.set('xmlns:wp', 'http://wordpress.org/export/1.2/')

channel = ET.SubElement(rss, "channel")

#ET.SubElement(channel, 'title').text = 'Brevity: A Journal of Concise Literary Nonfiction'
#ET.SubElement(channel, 'link').text = 'http://brevitymag.com'
#ET.SubElement(channel, 'description').text = 'Brevity: The journal devoted exclusively to the concise literary nonfiction.'

# wordpress required
ET.SubElement(channel, 'wp:wxr_version').text = '1.2'

# wordpress required
item = ET.SubElement(channel, "item")
ET.SubElement(item, 'title').text = 'This is title'
ET.SubElement(item, 'dc:creator').text = '<![CDATA[elhajj]]>'
ET.SubElement(item, 'description').text = 'This is the description'
ET.SubElement(item, 'content:encoded').text = '<![CDATA[This is the story]>'
ET.SubElement(item, 'excerpt:encoded').text = '<![CDATA[This is an exerpt]>'
ET.SubElement(item, 'wp:post_date').text = '2000-01-01 19:20:00'
ET.SubElement(item, 'wp:status').text = 'draft'
ET.SubElement(item, 'wp:type').text = 'post'


tree = ET.ElementTree(rss)
#print type(tree), "this is the tree"
#tree = ET.parse(tree)
root = tree.getroot()

for child in root[0][1]:
    print child.text

title2 = 'This is a new title'
story = 'This is a new story'

print '\n\n'

root[0][1][0].text = title2
root[0][1][2].text = str(' ')
root[0][1][3].text = story
root[0][1][1].text = str('elhajj')

for child in root[0][1]:
    print child.text

#for i in item:
#    i.text = str(title2)
#    i.text = str(story)


tree.write("filename.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml"
           )


# https://wordpress.stackexchange.com/questions/82399/what-is-the-required-format-for-importing-posts-into-wordpress
# http://stackoverflow.com/questions/4997848/emitting-namespace-specifications-with-elementtree-in-python