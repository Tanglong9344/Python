# declare encoding(default ASCII)
# -*- coding:utf-

# int
print(1234)

# float
print(3.14)

# string
print("1234")
print("Welcome to Python")
print("Good boy\n")
print('"Good"boy\n')
print("'Good'boy\n")
print('I\'m a \"Good\" boy\n')
str1 = '*\n***\n*****\n***\n*'
print(str1)

str2 = '''
Stay hunGry,
stay foolish.
-- Steve Jobs
'''
print(str2)

s1 = "Hello"
s2 = "World!"
print(s1)
print(s2)
print(s1+s2)
s = s1+s2
print(s)

s += "2017"
print(s)

print('This year is %d' % 2017)
print('This year is %d' % 20.17)
print('This year is %f' % 20.17)
print("Do you know %s" % s)

# string's catentation
print("Hello" + "Python!")

# print with loop
# --1
for j in range(1, 6):
    print('* ' * j)
print()

# --2
for i in range(0, 5):
    for j in range(0, 5):
        print('* ', end='')
    print()
print()

# --3
for i in range(0, 5):
    print('* ' * 5)
print()

# --4
for i in range(0, 5):
    for j in range(0, i + 1):
        print('* ', end=''),
    print()
print()

# Mutiply table
for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d = %2d\t" % (j, i, i * j), end='')
    print()

# number-1
for i in range(1, 4):
    for j in range(1, 5):
        print("%d" % i * j)

# number-2
for i in range(1, 4):
    for j in range(1, 5):
        print("%d" % (i * j))

# number-3
for i in range(1, 4):
    for j in range(1, 5):
        print("%d*%d = %2d" % (i, j, i * j))

# if the file is executed, the '__name__' will be '__main__'
print(__name__)
