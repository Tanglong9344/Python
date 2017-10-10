#错误处理
#出现错误则终止try：内程序的执行，转向exception：
#跳过出错部分而不会终止整个程序
try:
    f = open('non-exist.txt')
    print ('File opened!')
    f.close()
except:
    print ('File not exists.')
print('Done')