# python urllib.request module
import urllib.request
import json
import re

web = urllib.request.urlopen('http://www.baidu.com')
content = web.read()
fp = open("baidu.html",'wb')
fp.write(content)
fp.close()