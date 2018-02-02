# A function without parameters
# Build-in Functions: https://docs.python.org/3/library/functions.html


def hello():
    print("Hello!")


# Call the function
hello()

# A function with a parameter


def mysum(n):
    s = 0
    for i in range(1, n):
        s += i
    return s


# Call the Function


print(mysum(11))

# A function with two parameters


def myadd(a, b):
    return a + b


# Call the Function
print(myadd(1, 3))

# A function with default value


def hello(name='World!'):
    print("Hello " + name)


hello()
hello("Python!")

# variable parameters--in fact it's tuple


def varsTuple(arg, *args):
    print("arg=", arg)
    for x in args:
        print(x, end=', ')
    print()


varsTuple("para")
varsTuple(1, 3, 5, 7, 9)

# anonymous function(lambda)
mySum = lambda a, b:a + b

print("mySum: ", mySum(3, 4))

# return


def mysum2(a, b):
    return a + b


print("mysum2:", mysum2(5, 7))

# mysum2 in another form


def mysum22(s, a, b):
    print(s, a + b)


# deliver position argument--have to deliver arguments in right order
mysum22("form1:", 1, 2)
# deliver keyword argument--don't have to deliver arguments in right order
# this is realised by a data structure called dictionary
mysum22(s="form2:", a=1, b=2)

# key words parameters


def print_str(str0):
    print(str0)


print_str(str0="Hello Python function...")

# global variable
xx = 12


def test_global():
    global xx
    xx = 33


print('Before test_global, xx=', xx)
test_global()
print('After test_global, xx=', xx)


# docString


def test_docString():
    '''This is a test about docString

    You can get the detail by \'__doc__\'.'''
    pass


print(test_docString.__doc__)
