# 进度条
import sys
import time

# print progress of a point


def bar(num, total):
    r = '\r[%s%s]%d%%' % ("=" * num, " "*(total-num), num, )
    sys.stdout.write(r)
    sys.stdout.flush()


N = 100
TIME = 0.1
if __name__ == '__main__':
    for i in range(0, N + 1):
        time.sleep(TIME)
        bar(i, N)
