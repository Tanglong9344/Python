import threading
import time

import requests


class Test():
        # 数据发送
        def data_post(self):
            data = [{},{},{}]
            try:
                url = "http://www.likeban.tech:8080/gar/tem/save"
                data = '{"data:' + str(data) + '"}'
                res = requests.post(url=url, data=data)
                print(res.text)
            except Exception as e:
                print('data post error:', e)

if __name__ == '__main__':
    test = Test()
    cnt = 0
    while True:
        cnt += 1
        time.sleep(0.01)
        if cnt % 100 == 0:
            print('xxxxxxxxxxxxxxxx%dxxxxxxxxxxxxxxxxxxxx'%cnt)
            t1 = threading.Thread(target=test.data_post())
            t1.start()