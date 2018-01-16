from random import choice
# list
print("--1: ")
list0 = range(1, 10)
for i in list0:
    print("%d " % i, end='')
print()
print(list0)

# --2, list can contain all kinds of types
print("--2: ")
list0 = [1, 3, 'stringing', True, 9, False, 17, 3.14, 3 + 2j, [3, True, "list"], {12, "dictionary", 6.28}]
print("length: ", len(list0))
print(list0 + ['catenation'])
print("stringing" in list0)
print(["AAA"]*3)
print(list0)
# --3
print("--3: ")
list0 = ['meat', 'egg', 'fish', 'milk']
for i in list0:
    print("%s " % i, end='')
print()
print(list0)

# --4
print("--4: ")
list0 = ['meat', 'egg', 'fish', 'milk']
for i in range(0, 4):
    print("%s " % list0[i], end='')
print()
print(list0)

# --5 modify
print("--5, modify: ")
list0[0] = 'animals'
list0[1] = 'birds'
list0[2] = 'water'
list0[3] = 'cups'
print(list0)

# --6 concatenate
print("--6, cat: ")
llist0 = ['bread', 'noodle', 'fruit', 'smile']
list0 += llist0
print(list0)

# --7 add
print("--7, add: ")
list0.append('Hello Python!')
print(list0)

# --8，delete
print("--8, del: ")
list0 = ['meat', 'egg', 'fish', 'milk']
del list0[0]
print(list0)

# --9，index and section
print("--9: ")
list0 = ['meat', 'egg', 'fish', 'milk', 'fruit']
print(list0)
print(list0[-1])  # the last one
print(list0[-3])

print(list0[1:3])
print(list0[:3])
print(list0[1:])
print(list0[:])  # list0[ : ] <=> list0[0 : -1]
print(list0[1:-1])

# --10，using choice to randomly choose from a list
print("--10: ")
lis = ['meat', 'egg', 'milk', 'fruit', 'fish']
time = 0
N = 3
while time < N:
    print("From the list you randomly get: " + choice(lis))
    time += 1

# list methods
print(list0)

list0.append("egg")
list0.insert(-1, "egg")
print(list0)

print(list0.count("egg"))

list0.reverse()  # 翻转
print(list0)

list0.sort()     # 排序
print(list0)

list0.pop(-1)
print(list0)

list0.remove("egg")  # remove the first one that meets the condition
print(list0)
