# 获取可用的代理服务器IP
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re


def gethtml(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsobj = BeautifulSoup(html.read(), 'lxml')
        labellist = bsobj.findAll('td')
    except AttributeError as e:
        print(e)
        return None
    return labellist


def getdict(html):
    regip = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    regp = re.compile('\d{1,4}\d$')
    dict = {}
    for item in html:
        if regip.match(item.get_text()):
            key = item.get_text()
        if regp.match(item.get_text()):
            value = item.get_text()
            dict[key] = value
    return dict


def fwrite(dict, fname):
    file = open(fname, 'a')
    for key in dict:
        file.write(key + ':' + dict[key] + '\n')
    file.close()


if __name__ == '__main__':
    url = 'http://www.66ip.cn/'
    fname = 'poxy.txt'
    for page in range(1, 20):
        if page == 1:
            newurl = url + 'index.html'
        else:
            newurl = url + str(page) + '.html'
        html = gethtml(url)
        dict = getdict(html)
        fwrite(dict, fname)
        print(u'完成第' + newurl + u'页')
    print(u'写入成功')
