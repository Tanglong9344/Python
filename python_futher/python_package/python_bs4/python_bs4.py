# python package 'bs4--beautiful soup4'
# Beautiful Soup 4.4.0 文档: http://beautifulsoup.readthedocs.io/zh_CN/latest/
from bs4 import BeautifulSoup

fp = open('test_bs4.html', 'r')
html_doc = fp.read()
fp.close()

print('----------Before parse-------------')
print(html_doc)

soup = BeautifulSoup(html_doc, "html.parser")
print('----------After  parse-------------')
print(soup.prettify())

# structural data
print('title:', soup.title)
print('meta:', soup.meta)
print('body:', soup.body)
print('div:', soup.div)
print('a:', soup.a)
print('h1:', soup.h1)

# get all links
cnt = 1
for link in soup.find_all('a'):
    print('link%d:'% cnt, link)
    cnt += 1
