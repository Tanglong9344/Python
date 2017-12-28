# python closure-have the ability to visit local variable in a function

# nested function
def fun_nested(str):
    # inner function
    def fun_in():
        print(str)
    # call the inner function
    fun_in()

# call the nested function
fun_nested("Nested function...")

# closure function-1
def fun_closure_1(str):
    # inner function
    def fun_in():
        print(str)
    # return inner function
    return fun_in

# call the closure function-1
fun_obj = fun_closure_1("Closure function...")
fun_obj()

# closure function-2
def fun_closure_2(a):
    # inner function
    def fun_in(b):
        return a + b
    # return inner function
    return fun_in

# call the closure function-2
fun_obj2 = fun_closure_2(3)
result = fun_obj2(4)
print("result=", result)
print("result=", fun_closure_2(3)(4)) # a more simple way to call closure function

print(fun_closure_2(3).__closure__)
print(fun_closure_2(3).__closure__[0].cell_contents)
