# 整型
i = 110
print(type(i),end=',')
print("i:",  i)
print("0x110:", 0x110) # 十六进制
print("0o110:", 0o110) # 八进制
# 浮点数
f = 9.99
print(type(f), end=', ')
print(f)
# 复数
c = 2 + 3j
print(type(c), end=', ')
print(c)
# 字符串
str = 'Tang long'
print(type(str), end=', ')
print(str)
# 布尔值
b = True
print(type(b), end=', ')
print(b)

# 多重赋值
i2, f2, str2, b2, c2 = 1101, 9.999, 'Tang longg', False, 2j+3
print(i2, end=', ')
print(f2, end=', ')
print(str2, end=', ')
print(b2, end=', ')
print(c2)
