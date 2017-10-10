# 形状其一
for j in range(1, 6):
    print('*' * j)
print()

# 形状其二
for i in range(0, 5):
    for j in range(0, 5):
        print('*', end='')
    print()
print()

# 形状其三
for i in range(0, 5):
    print('*' * 5)
print()

# 形状其四
for i in range(0, 5):
    for j in range(0, i + 1):
        print('*', end=''),
    print()
print()

# 乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d=%2d\t" % (j, i, i * j), end='')
    print()

# 直角数字三角形
for i in range(1, 4):
    for j in range(1, 5):
        print("%d" % i * j)

# 对比1
for i in range(1, 4):
    for j in range(1, 5):
        print("%d" % (i * j))

# 对比2
for i in range(1, 4):
    for j in range(1, 5):
        print("%d*%d=%2d" % (i, j, i * j))