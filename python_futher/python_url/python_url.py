# python urllib.request module
import urllib.request
import json
import re

web = urllib.request.urlopen('http://www.baidu.com')
content = web.read()
re.sub('\n',content,'')
re.sub('\t',content,'')
fp = open("baidu.html",'wb')
fp.write(content)