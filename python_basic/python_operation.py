a = 10
b = 3
# arithmetic operation
print("+  : ", a + b)
print("-  : ", a - b)
print("*  : ", a * b)
print("/  : ", a / b)
print("%  : ", a % b)   # 取余
print("** : ", a ** b)  # 幂运算
print("// : ", a // b)
print("// : ", -a // b) # 向下取整
# logical operation
print("== : ", a == b)
print("<  : ", a < b)
print("<= : ", a <= b)
print(">  : ", a > b)
print(">= : ", a >= b)
print("!= : ", a != b)

# bit operation
# a:1010(2),b:0011(2)
print("&  : ", a & b)
print("|  : ", a | b)
print("^  : ", a ^ b)
print("~  : ", ~a)     # 按位取反(8位),
                       # 0 000 1010->0 000 1010(补码)
                       # 0 000 1010->1 111 0101(按位取反)
                       # 1 111 0101->1 000 1010(补码)
                       # 1 000 1010->1 000 1011(末位加1)
# ~-11:1 000 1011->1 000 1010(末位减1)->1 111 0101(符号位不变，其它位取反)->0 000 1010->0 000 1010
print(">> : ", a >> b) # 右移b位
print("<< : ", a << b) # 左移b位

# bool operation
print("and: ", a and b)  # b
print("or : ", a or b)   # a
print("not: ", not a)    # False

# scientific notation(based on 10)
print(3e2)
print(3e-2)

# is and is not
print("is:", a is b)
print("is not:", a is not b)
