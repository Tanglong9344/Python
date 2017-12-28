# python decorator
# Everything in python is object
# meta-programming

# method as a object in python
def m_str(str):
    print(str)

m_str("Python...")
m1 = m_str
m2 = m1
m1("m1, Python...")
m2("m2, Python...")

print("name:\n",m_str.__name__, m1.__name__, m2.__name__)
print("code:\n",m_str.__code__,"\n", m1.__code__,"\n", m2.__code__)

# high-order function
def add(x,y):
    return x + y

def substract(x,y):
    return x -y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def operator(fun,x,y):
    return fun(x,y)

print(operator(add,3,4))
print(operator(substract,3,4))
print(operator(multiply,3,4))
print(operator(divide,3,4))

# decorator-receive a function and add something new to it
def fun_old():
    print("Before decorated...")

def fun_new(fun):
    def decorator():
        fun()
        print("After decorator...")
    # return new function
    return decorator

# decorator--1
# before
fun_old()
# decorator
fun_old = fun_new(fun_old)
#after
fun_old()

# decorator--2
@fun_new     # (@ + decorator function)
def fun_old():
    print("Before decorated...")
#after
fun_old()

# decorator parameter-if divided by zero ,will return None
def smart_divide(func):
   def inner(a,b):
      if b == 0:
         print("Can't divided by 0...")
         return
      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(3,0))


# multiple decorator
def star(func):
    def inner(n):
        print("*" * n)
        func(n)
        print("*" * n)
    return inner

def percent(func):
    def inner(n):
        print("%" * n)
        func(n)
        print("%" * n)
    return inner

# decorate --1
@star
@percent
def printer(n):
    pass

printer(66)

print("\n")
# decorate --2
def printer2(n):
    pass
printer2=star(percent(printer2))
printer2(66)

