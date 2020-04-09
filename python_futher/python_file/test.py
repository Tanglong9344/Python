try:
    fp = open("test2.txt", "a")
except Exception as e:
    print('open file failed:',e)
    fp = open("test2.txt", "w")
data=[]
data.append('I am  coming')
data.append('I am  coming2')
data.append('I am  coming2')
for i in data:
    fp.write('\n'+i)
fp.close()