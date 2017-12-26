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
        print("%d*%d=%2d\t" % (j, i, i * j), end='')
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
        print("%d*%d=%2d" % (i, j, i * j))