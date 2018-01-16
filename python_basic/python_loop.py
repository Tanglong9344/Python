# for
n = 11
s = 0
for i in range(1, n):
    print(i, end='')
    if i < n-1:
        print('+', end='')
    s += i
print(" = ", end='')
print(s)

# while
s = 0
i = 1
while i < n:
    print(i, end='')
    if i < n-1:
        print('+', end='')
    s += i
    i += 1
print(" = %d" % s)

# reverse print
for i in range(n, -1, -1):  # 左闭右开区间(satrt, end, step)
    print(i, end=', ')
print()
# print vs vreverse print
for i in range(-1, n, 1):
    print(i, end=', ')

# 九九乘法表==1
print("\nFormat--1:")
for i in range(1,10):
    for j in range(1,10):
        print('{0:d}X{1:d}={2:2d}'.format(i,j,i*j),end=' ')
    print()

# 九九乘法表==1
print("\nFormat--2:")
for i in range(1,10):
    for j in range(1,10):
        print('%dX%d=%2d' %(i,j,i*j),end=' ')
    print()
