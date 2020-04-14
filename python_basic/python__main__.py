import sys
import datetime

if __name__ == '__main__':
    print(sys.argv)
    print("__name__=", __name__)

    print(str(datetime.datetime.now()))
    print((datetime.datetime.now() + datetime.timedelta(0)).strftime("%Y-%m-%d"))