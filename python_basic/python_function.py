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