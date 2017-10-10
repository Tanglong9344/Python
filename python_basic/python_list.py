#python 是弱类型语言
#list
#形式1
print ("形式1：")
l = range(1, 10)
for i in l:
    print ("%d "%i,end='')
print()
print (l)

#形式2
print ("形式2：")
l = [1,3,6,7,9,13,17,99,111]
for i in l:
    print ("%d "%i,end='')
print ()
print (l)

#形式3
print ("形式3：")
l = ['meat', 'egg', 'fish', 'milk']
for i in l:
    print ("%s "%i,end='')
print ()
print (l)

#形式4
print ("形式4：")
l = ['meat', 'egg', 'fish', 'milk']
for i in range (0, 4):
    print ("%s "%l[i],end='')
print ()
print (l)

#形式5,修改
print ("形式5：")
l = ['meat', 'egg', 'fish', 'milk']
l[0] = 'animals'
l[1] = 'birds'
l[2] = 'water'
l[3] = 'cups'
for i in range (0, 4):
    print ("%s "%l[i],end='')
print ()
print (l)

#形式6，连接
print ("形式6：")
l = ['meat', 'egg', 'fish', 'milk']
ll = ['bread','noodle','fruit','smile']
l += ll
for i in range (0, 8):
    print ("%s "%l[i],end='')
print ()
print (l)

#形式7，添加
print ("形式7：")
l = ['meat', 'egg', 'fish', 'milk']
l.append('HelloWorld')
for i in range (0, 5):
    print ("%s "%l[i],end='')
print ()
print (l)

#形式8，删除
print ("形式8：")
l = ['meat', 'egg', 'fish', 'milk']
del l[0]
for i in range (0, 3):
    print ("%s "%l[i],end='')
print ()
print (l)

#形式9，索引和切片
print ("形式9：")
l = ['meat', 'egg', 'fish', 'milk','fruit']
print (l[-1]) #返回最后一个
print (l[-3])

print (l[1:3]) #返回第二个到第三个之间的两个
print (l[ :3])
print (l[1: ])
print (l[ : ]) #l[ : ] <=> l[0 : -1]
print (l[1:-1])

#形式10，choice 用于从list之中随机选择
print ("形式10：")
list = ['meat', 'egg', 'milk', 'fruit', 'fish']
from random import choice
time = 0
N = 5
while time < N:
    print ("From list you got: "+choice(list))
    time += 1