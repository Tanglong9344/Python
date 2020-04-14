from threading import Timer

# 非阻塞

def printHello1():
    print('Hello Python 111111111!')
    Timer(2, printHello1).start()

def printHello2():
    print('Hello Python 22222222222!')
    Timer(2, printHello2).start()

if __name__ == '__main__':
    printHello1()
    printHello2()
