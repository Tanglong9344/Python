import threading

class Test():
    def __init__(self):
        self.cnt = 0
        self.cnt2 = 0

    def fun1(self):
        self.cnt2 += 1
        print('cnt22222:', self.cnt2)
        for i in range(0, self.cnt):
            print('Fun111111111:xxx%d' % i)

    def fun2(self):
        print('222222222222222')
        print('cnt11111111:',self.cnt)
        self.cnt += 1

if __name__ == '__main__':
    test = Test()
    test.cnt = 0
    while True:
        t2 = threading.Thread(target=test.fun2)
        t2.start()
        print('ccccccccccccc:',test.cnt)
        print('TTTTTTTTTTTT:',test.cnt2)
        if test.cnt > 100:
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            t1 = threading.Thread(target=test.fun1)
            t1.start()
        if t2.is_alive():
            print('AAAAAAA22222222AAAAAAAAAA')
        print('cnt2:', test.cnt2)
        if test.cnt2 >= test.cnt:
            test.cnt2 = 0
            print('YYYYYYYYYYYYYYYYY:',test.cnt2)