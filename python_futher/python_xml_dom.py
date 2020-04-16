import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("poem.xml")
collection = DOMTree.documentElement
# Get all the poem in the collection
poems = collection.getElementsByTagName("poem")
# Print detail of each poem.
for poem in poems:
    print("*****poem*****")
    # country
    if poem.hasAttribute("country"):
        print("朝代: %s" % poem.getAttribute("country"))
    # author
    if poem.hasAttribute("author"):
        print("作者: %s" % poem.getAttribute("author"))
    # title
    title = poem.getElementsByTagName('title')[0]
    print("标题: %s" % title.childNodes[0].data)
    # content
    content = poem.getElementsByTagName('content')[0]
    print("内容: %s" % content.childNodes[0].data)