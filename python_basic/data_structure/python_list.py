# list:有序，可变
from random import choice
#number
myList = range(1, 10)
for i in myList:
    print("%d " % i, end='')
print()
print(myList)
# string
myList = ['meat', 'egg', 'fish', 'milk']
for i in myList:
    print("%s " % i, end='')
print()
print(myList)

myList = ['meat', 'egg', 'fish', 'milk']
for i in range(0, 4):
    print("%s " % myList[i], end='')
print()
print(myList)
# other types
myList = [1, 3, 'stringing', True, 9, False, 17, 3.14, 3 + 2j, [3, True, "list"], {12, "dictionary", 6.28}]
print("length: ", len(myList))
print(myList)
print(myList + ['catenation'])
print("stringing" in myList)
print(["AAA"]*3)

myList[0] = 'animals'
myList[1] = 'birds'
myList[2] = 'water'
myList[3] = 'cups'
print(myList)

# concatenate
lmyList = ['bread', 'noodle', 'fruit', 'smile']
myList += lmyList
print(myList)

# add
myList.append('Hello Python!')
print(myList)

# delete
myList = ['meat', 'egg', 'fish', 'milk']
del myList[0]
print(myList)

# index and section
myList = ['meat', 'egg', 'fish', 'milk', 'fruit']
print(myList)
print(myList[-1])  # the last one
print(myList[-3])

print(myList[1:3])
print(myList[:3])
print(myList[1:])
print(myList[:])  # myList[ : ] <=> myList[0 : -1]
print(myList[1:-1])

# using choice to randomly choose from a list
myList = ['meat', 'egg', 'milk', 'fruit', 'fish']
time = 0
N = 3
while time < N:
    print("From the list you randomly get: " + choice(myList))
    time += 1

print(myList)

myList.append("egg")
myList.insert(-1, "egg")
print(myList)

print(myList.count("egg"))

myList.reverse()  # 翻转
print(myList)

myList.sort()     # 排序
print(myList)

myList.pop(-1)
print(myList)

myList.remove("egg")  # remove the first one that meets the condition
print(myList)

myList = [12, [34,'sublist'], ['sublist2', [66, 88]], 'list', [True, False]]
print(myList)

# reference -- refer to the memory where the object is stored
test = [1, 2, 3, 4, 5, 6]
test1 = test
del test1[0]
print(test1)
print(test)

test2 = test[:]  # make a copy by doing a full slice
del test2[0]
print(test2)
print(test)

# 数组排序(元素为set,指定set内的key进行排序)
data = [{'a':1.0},{'a':6.5},{'a':3.14}]
data=sorted(data,key=lambda i:i['a'])[::-1]
print(data)

# 向数组头部添加元素
data = [1,2,3]
print(data)
data.insert(0,4)
print(data)

data.reverse()
print('after reverse:',data)
data.append(5)
data.reverse()
print(data)