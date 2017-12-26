# exception
try:
    f = open('non-exist.txt')
    print ('File opened.')
    f.close()
except:
    print ('File not find...')
print('Done.')