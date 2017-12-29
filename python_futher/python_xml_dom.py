# python XML parse in dom
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("poem.xml")
collection = DOMTree.documentElement
# Get all the poem in the collection
poems = collection.getElementsByTagName("poem")
# Print detail of each poem.
for poem in poems:
   print ("*****poem*****")
   # address
   if poem.hasAttribute("address"):
      print ("Address: %s" % poem.getAttribute("address"))
    # author
   if poem.hasAttribute("author"):
      print ("Author: %s" % poem.getAttribute("author"))
    # title
   title = poem.getElementsByTagName('title')[0]
   print ("Title: %s" % title.childNodes[0].data)
   # description
   description = poem.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)