import xml.etree.ElementTree as ET

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
ET.SubElement(channel, 'pubDate').text = 'Fri, 28 Apr 2017 21:01:20 +0000'
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
ET.SubElement(category, 'wp:category-nicename').text = 'issue-29-2009'
ET.SubElement(category, 'wp:category-parent').text = None
ET.SubElement(category, 'wp:cat_name').text = 'Issue 29 / January 2009'

item = ET.SubElement(channel, "item")
ET.SubElement(item, 'title').text = None
ET.SubElement(item, 'link').text = None
ET.SubElement(item, 'pubDate').text = None
ET.SubElement(item, 'dc:creator').text = None
ET.SubElement(item, 'guid', isPermaLink='false' ).text = None
ET.SubElement(item, 'description').text = None
ET.SubElement(item, 'content:encoded').text = None
ET.SubElement(item, 'excerpt:encoded').text = None
ET.SubElement(item, 'wp:post_id').text = None
ET.SubElement(item, 'wp:post_date').text = '2000-01-01 19:20:00'
ET.SubElement(item, 'wp:post_date_gmt').text = None
ET.SubElement(item, 'wp:comment_status').text = 'open'
ET.SubElement(item, 'wp:ping_status').text = 'open'
ET.SubElement(item, 'wp:post_name').text = None
ET.SubElement(item, 'wp:status').text = 'publish'
ET.SubElement(item, 'wp:post_parent').text = '0'
ET.SubElement(item, 'wp:menu_order').text = '0'
ET.SubElement(item, 'wp:type').text = 'post'
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

for child in root[0][10]:
    print child.text

title2 = 'This is a new title'
creator = 'elhajj'
story2 = 'This is a new story'

title2 = CDATA(title2)
creator = CDATA(creator)
story2 = CDATA(story2)

root[0][10][0].append(title2)
root[0][10][3].append(creator)
root[0][10][6].append(story2)

for child in root[0][10]:
    print child.text, 'after'


tree.write("filename.xml",
           xml_declaration=True, encoding='utf-8',
           method="xml"
           )


# https://wordpress.stackexchange.com/questions/82399/what-is-the-required-format-for-importing-posts-into-wordpress
# http://stackoverflow.com/questions/4997848/emitting-namespace-specifications-with-elementtree-in-python