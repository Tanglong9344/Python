#list
print ("--1: ")
l = range(1, 10)
for i in l:
    print ("%d "%i, end='')
print()
print (l)

#--2, list can contain all kinds of types
print ("--2: ")
l = [1,3,"stringing",True,9,False,17,3.14,3+2j,[3,True,"list"],{12,"dictionary",6.28}]
print (l)

#--3
print ("--3: ")
l = ['meat', 'egg', 'fish', 'milk']
for i in l:
    print ("%s "%i, end='')
print ()
print (l)

#--4
print ("--4: ")
l = ['meat', 'egg', 'fish', 'milk']
for i in range (0, 4):
    print ("%s "%l[i], end='')
print ()
print (l)

#--5 modify
print ("--5, modify: ")
l[0] = 'animals'
l[1] = 'birds'
l[2] = 'water'
l[3] = 'cups'
print (l)

#--6 concatenate
print ("--6, cat: ")
ll = ['bread','noodle','fruit','smile']
l += ll
print (l)

#--7 add
print ("--7,add: ")
l.append('Hello Python!')
print (l)

#--8，delete
print ("--8, del: ")
l = ['meat', 'egg', 'fish', 'milk']
del l[0]
print (l)

#--9，index and section
print ("--9: ")
l = ['meat', 'egg', 'fish', 'milk','fruit']
print(l)
print (l[-1]) # the last one
print (l[-3])

print (l[1:3])
print (l[ :3])
print (l[1: ])
print (l[ : ]) #l[ : ] <=> l[0 : -1]
print (l[1:-1])

#--10，using choice to randomly choose from a list
print ("--10: ")
list = ['meat', 'egg', 'milk', 'fruit', 'fish']
from random import choice
time = 0
N = 3
while time < N:
    print ("From the list you randomly get: "+choice(list))
    time += 1
