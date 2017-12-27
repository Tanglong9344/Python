# A function without parameters
def hello():
    print("Hello!")

# Call the function
hello()

# A function with a parameter
def mysum(n):
    s=0
    for i in range (1,n):
        s += i
    return s

# Call the Function
print (mysum(11))

# A function with two parameters
def myadd(a,b):
    return a + b

# Call the Function
print(myadd(1,3))

# A function with default value
def hello (name = 'World!'):
    print ("Hello " + name)

hello()
hello("Python!")

# variable parameters
def vars(arg, *args):
    print("arg=", arg)
    for x in args:
        print(x, end=',')
    print()

vars("para")
vars(1,3,5,7,9)

# anonymous function(lambda)
mysum = lambda a, b: a + b

print("mysun: ", mysum(3,4))

# return
def mysum2(a,b):
    return a + b

print("mysum2:", mysum2(5,7))

# key words parameters
def print_str(str):
    print(str)
print_str(str = "Hello Python function...")