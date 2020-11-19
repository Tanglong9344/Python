import pymysql
import requests
from bs4 import BeautifulSoup as BS

def Get_data():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie': 'acw_tc=6f3e47cc15498749418558688e3d6410ea97be9a552b180841c5079605; PHPSESSID=s2hjdg3slh32omchfsib4himk0; UM_distinctid=168dbbfe8c533e-0e42df11c1c0a7-9393265-100200-168dbbfe8c71088; CNZZDATA1256319371=345851669-1549873534-%7C1549873534; CNZZDATA1257119496=134880590-1549870452-%7C1549870452; Hm_lvt_a48e6ab107a4e68d47e6fdb5d83961e5=1549875015; Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1549875021; CNZZDATA1254708131=653924416-1549874976-%7C1549874976; CNZZDATA1275922735=1673340420-1549874690-%7C1549874690; CNZZDATA1257131565=1820590917-1549873827-%7C1549873827; CNZZDATA1257125147=1301871275-1549871347-https%253A%252F%252Fwww.duanwenxue.com%252F%7C1549871347; Hm_lpvt_a48e6ab107a4e68d47e6fdb5d83961e5=1549875906; Hm_lpvt_3c8ecbfa472e76b0340d7a701a04197e=1549875913; ajax_award_timestamp=1549875887; ajax_award_timestamp__ckMd5=706904497e9c8dfd; ajax_award_key=94a17405d22ab8aacbabbbfdb9d4740c; ajax_award_key__ckMd5=3e97bde02ab1998d',
    'referer': 'https://www.duanwenxue.com/huayu/tianyanmiyu/list_69.html',
    'upgrade-insecure-requests': '1'
    }
    articles = []
    i=0
    while len(articles) < 366:
        url = 'https://www.duanwenxue.com/huayu/tianyanmiyu/list_{}.html'.format(i)
        i = i+1
        response = requests.get(url, headers=headers)
        text=response.text
        if text:
            soup = BS(text, 'lxml')
            arttis = soup.find('div', class_='list-short-article').find_all('a', {'target': "_blank"})
            for t in arttis:
                articles.append(t.text.strip())
    save_text(articles)

def save_text(articles):
    db = pymysql.connect("localhost", "root", "password", "tl")
    cursor = db.cursor()
    for i in range(len(articles)):
        print("xx:",i+1)
        print(articles[i])
        sql = "INSERT INTO love_word(id,word) VALUES (%d,'%s')" %(i+1,articles[i]);
        cursor.execute(sql)
        db.commit()

if __name__ == '__main__':
    Get_data()