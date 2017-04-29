import xml.etree.ElementTree as ET

rss = ET.Element("rss")
channel = ET.SubElement(rss, "channel")

#ET.SubElement(doc, "field1", name="blah").text = "some value1"
#ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

#headers
'''
<rss 
xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" 
xmlns:content="http://purl.org/rss/1.0/modules/content/" 
xmlns:wfw="http://wellformedweb.org/CommentAPI/" 
xmlns:dc="http://purl.org/dc/elements/1.1/" 
xmlns:wp="http://wordpress.org/export/1.2/" version="2.0">

'''
tree = ET.ElementTree(rss)
tree.write("filename.xml")

# https://wordpress.stackexchange.com/questions/82399/what-is-the-required-format-for-importing-posts-into-wordpress
# http://stackoverflow.com/questions/4997848/emitting-namespace-specifications-with-elementtree-in-python