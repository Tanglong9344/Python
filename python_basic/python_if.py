from random import randint

x = randint(1, 10)
if x == 1:
    print("X is One")
elif x == 2:
    print("X is Two")
else:
    print("The range is too huge!")
print("The X is :%d" % x)

# nested if open-up and shut-down circuit
a = randint(0, 10)
b = randint(0, 10)
if a > 0:
    if b > 0:
        print("open")
    else:
        print("shutdown")
else:
    print("shutdown")
print("a: %d, b: %d" % (a, b))
