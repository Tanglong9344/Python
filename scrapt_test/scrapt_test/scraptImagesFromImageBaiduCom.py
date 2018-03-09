# -*- coding:utf-8 -*-
# reference: https://github.com/nnngu/LearningNotes/blob/master/Spider/02%20Python%E7%88%AC%E8%99%AB%
# E5%AE%9E%E7%8E%B0%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87%E8%87%AA%E5%8A%A8%E4%B8%8B%E8%BD%BD.md

import re
import requests
from urllib.parse import *


def download_pic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    print('KeyWord: ' + keyword + ', Start downloading...')
    for each in pic_url:
        print('Downloading the ' + str(i) + ' piece of picture，URL:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('Something wrong hanppened!')
            continue

        dest_dir = 'images/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dest_dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    word = input("Input key word: ")
    print(word)
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=' + word + '&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
    result = requests.get(url)
    download_pic(result.text, word)
