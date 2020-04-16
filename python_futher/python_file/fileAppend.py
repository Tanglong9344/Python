try:
    fp = open("test2.txt", "a")
    for i in range(0,3):
        fp.write('I am  coming%d\n'%(i+1))
    fp.close()
except Exception as e:
    print('open file failed:',e)
    fp = open("test2.txt", "w")